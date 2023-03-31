# DFS, Topological Sort, BFS
class Solution:

    # Topological Sort, and then check order of each prerequisite pair
    # TODO: remove the nested function
    def canFinish_topological_sort(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def topological(graph: List[List[int]], visited: List[int], s: List[int], i: int) -> None:
            if visited[i]:
                return
            visited[i] = True
            for t in graph[i]:
                topological(graph, visited, s, t)
            s.append(i)

        graph = [[] for _ in range(numCourses)]
        visited = [False for _ in range(numCourses)]
        stack = []
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
        for i in range(numCourses):
            topological(graph, visited, stack, i)
        
        order = [0 for _ in range(numCourses)]
        count = 0
        while stack:
            course_idx = stack.pop()
            order[course_idx] = count
            count += 1
        for prereq in prerequisites:
            if order[prereq[0]] <= order[prereq[1]]:
                return False
        return True


    # BFS to detect loop via indegree
    def canFinish_BFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for prereq in prerequisites:
            f, t = prereq[1], prereq[0]
            graph[f].append(t)
            indegree[t] += 1
        
        queue = []
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        count = 0
        while queue:
            curr = queue.pop(0)
            count += 1
            for t in graph[curr]:
                indegree[t] -= 1
                if indegree[t] == 0:
                    queue.append(t)

        return count == numCourses
    
    
    # adjacency list from course -> [prerequisites of this course]  
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def dfs_check_prereq(prerequisites: List[List[int]], visited: int, i: int) -> bool:
            if visited[i] == -1:
                return False
            elif visited[i] == 1:
                return True
            
            visited[i] = -1  # indicating currently just start searching prereq but not already satisfy all its prereq
            for prereq in prerequisites[i]:
                # check the status of prerequisites of the current node
                if not dfs_check_prereq(prerequisites, visited, prereq):
                    return False
            visited[i] = 1  # finished processing all the prereqs of the current node
            return True
        
        # the adjacency list stores all the prerequisites for course i
        prerequisites_adj = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for prereq in prerequisites:
            prerequisites_adj[prereq[0]].append(prereq[1])
        for course_idx in range(numCourses):
            if not dfs_check_prereq(prerequisites_adj, visited, course_idx):
                return False
        return True


    # build a graph (adjacency list) as in the regular way.
    def canFinish_v2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        self.has_cycle = False

        def dfs(graph: List[List[int]], visited: List[int], on_path: List[int], i: int) -> None:
            # During the process of looking for and checking all the prerequisites of some course, 
            # find a course already in the path, which means one (or more) prerequisites of this course
            # require this course as a prerequisite, and so that form a cycle.
            if on_path[i]:
                self.has_cycle = True
            if visited[i] or self.has_cycle:
                return
            visited[i] = True
            on_path[i] = True
            for t in graph[i]:
                dfs(graph, visited, on_path, t)
            on_path[i] = False

        graph = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
        visited = [False for _ in range(numCourses)]
        on_path = [False for _ in range(numCourses)]
        for course_idx in range(numCourses):
            dfs(graph, visited, on_path, course_idx)
        return not self.has_cycle

    

