# DFS, Topological Sort, BFS

from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        # Similar to 207. Course Schedule I
        # BFS with indegree
        # Constraint: The prerequisites graph has no cycles.
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for f, t in prerequisites:
            graph[f].append(t)
            indegree[t] += 1
        
        queue = []
        dependency = [set() for _ in range(numCourses)]
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        while queue:
            course = queue.pop(0)
            for t in graph[course]:
                for j in dependency[course]:
                    dependency[t].add(j)
                dependency[t].add(course)
                indegree[t] -= 1
                if indegree[t] == 0:
                    queue.append(t)

        res = []
        for u, v in queries:
            if u in dependency[v]:  # O(1)
                res.append(True)
            else:
                res.append(False)
        return res



# if __name__ == "__main__":
#     a = set()
#     a.add(2)
#     a.add(5)
#     a.add(5)
#     a.add(7)
#     a.discard(9)
#     print(a)
