# DFS, Topological Sort, BFS

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 0-indexed courses

        # build the graph(adjancency list: from -> [to_0, to_1, ...])
        graph = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            f = prerequisite[1]
            t = prerequisite[0]
            graph[f].append(t)
        
        # Topological Sort
        visited = [False for _ in range(numCourses)]
        stack = [] # used to store the res, reversed order!!!
        for v in range(numCourses):
            self.topological_sort(v, graph, visited, stack)
        
        # record order
        order = [-1 for _ in range(numCourses)]
        res = []  # to reverse elem in stack
        for i in range(len(stack)):
            course = stack.pop()
            order[course] = i
            res.append(course)
        for prerequisite in prerequisites:
            f, t = prerequisite[1], prerequisite[0]
            if order[f] >= order[t]:
                return []
        
        return res


    def topological_sort(self, v: int, graph: List[List[int]], visited: List[bool], stack: List[int]) -> None:
        if visited[v]:
            return
        visited[v] = True
        for t in graph[v]:
            self.topological_sort(t, graph, visited, stack)
        stack.append(v)
