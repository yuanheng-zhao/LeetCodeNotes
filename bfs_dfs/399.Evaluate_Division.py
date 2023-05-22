from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:


        # build the graph ***Notice: bidirecttional***
        # a -> {b->2.0, c->3.0}
        var2equations = {}
        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            val = values[i]
            if a not in var2equations:
                var2equations[a] = {a: 1.0}
            var2equations[a][b] = val
            if b not in var2equations:
                var2equations[b] = {b: 1.0}
            var2equations[b][a] = 1.0 / val
        
        ans = []
        print(var2equations)
        for query in queries:
            c = query[0]
            d = query[1]
            res = -1.0
            # BFS
            queue_var = [c]
            queue_val = [1.0]
            visited = set()
            while queue_var and res == -1.0: # while len(queue_var) != 0:
                curr_var = queue_var.pop(0)
                curr_val = queue_val.pop(0)
                # print(" current var ", curr_var, ", curr val ", curr_val)
                if curr_var in visited:
                    continue
                visited.add(curr_var)
                # print(" visited ", curr_var)

                if curr_var not in var2equations:
                    continue
                for var, val in var2equations[curr_var].items():
                    if var == d:
                        res = curr_val * val
                        break
                    if var in visited:
                        continue
                    queue_var.append(var)
                    queue_val.append(curr_val * val)
                    # print("     appended var ", var, ", val ", val)
            ans.append(res)
        
        return ans
