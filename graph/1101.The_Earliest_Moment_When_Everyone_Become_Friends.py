# Union Find

class Solution:

    class UF:
        def __init__(self, n: int) -> None:
            self.n = n
            self.union_count = n
            self.parent = {x: x for x in range(n)}

        # never used, but just put here
        def connected(self, x: int, y: int) -> bool:
            root_x = self.find_parent(x)
            root_y = self.find_parent(y)
            return root_x == root_y

        # path compression as well
        def find_parent(self, x: int) -> int:
            if self.parent[x] != x:
                self.parent[x] = self.find_parent(self.parent[x])
            return self.parent[x]

        def union(self, x: int, y:int) -> None:
            root_x = self.find_parent(x)
            root_y = self.find_parent(y)
            if root_x == root_y:
                return
            self.parent[root_x] = root_y
            self.union_count -= 1
            

    def earliestAcq(self, logs: List[List[int]], n: int) -> int:

        logs.sort(key=lambda x : x[0])  # sort first!!!

        uf = Solution.UF(n)
        for log in logs:
            timestamp, x, y = log[0], log[1], log[2]
            uf.union(x, y)
            if uf.union_count == 1:
                return timestamp

        return -1
