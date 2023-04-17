class Solution:
    def ways(self, pizza: List[str], k: int) -> int:

        m = len(pizza)
        n = len(pizza[0])
        mod = 10**9 + 7

        # construct a prefix sum matrix, accumulating from the right-bottom cell (m-1, n-1)
        # prefix_sum_mat(i,j): # of apples on pizza [(i,j), (m-1, n-1)]
        # Alternative: initialize a prefix sum matrix[m+1][n+1] w/ 0s, using a single nested for loop to calculate
        prefix_sum_mat = [[0 for _ in range(n)] for _ in range(m)]
        prefix_sum_mat[-1][-1] = 1 if pizza[-1][-1] == 'A' else 0
        for i in range(m-2, -1, -1):
            prefix_sum_mat[i][n-1] = prefix_sum_mat[i+1][n-1] + (1 if pizza[i][n-1] == 'A' else 0)
        for j in range(n-2, -1, -1):
            prefix_sum_mat[m-1][j] = prefix_sum_mat[m-1][j+1] + (1 if pizza[m-1][j] == 'A' else 0)
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                prefix_sum_mat[i][j] = prefix_sum_mat[i+1][j] + prefix_sum_mat[i][j+1] - prefix_sum_mat[i+1][j+1] + (1 if pizza[i][j] == 'A' else 0)
        # print(prefix_sum_mat)

        
        # dp(i,j,k'): # of ways of cutting pizza [(i,j), (m,n)] using k' cuts
        dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(k)]
        dp[0] = [[int(prefix_sum_mat[i][j] > 0) for j in range(n)] for i in range(m)]  # notice here
        for k in range(1, k):
            for i in range(m):
                for j in range(n):

                    for ii in range(i+1, m):
                        # if there exists at least one apple within the upper area
                        if prefix_sum_mat[i][j] - prefix_sum_mat[ii][j] > 0:
                            dp[k][i][j] += dp[k-1][ii][j]
                    for jj in range(j+1, n):
                        # if there exists at least one apple within the left area
                        if prefix_sum_mat[i][j] - prefix_sum_mat[i][jj] > 0:
                            dp[k][i][j] += dp[k-1][i][jj]

                    dp[k][i][j] %= mod

        return dp[-1][0][0]
