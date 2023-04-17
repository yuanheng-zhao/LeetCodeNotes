class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        m, n = len(matrix), len(matrix[0])
        self.mat = matrix  # original matrix
        
        # prefix sum: prefix_sum_mat[i][j] = sum of elements within the rectangle matrix[0, 0] to matrix[i, j] inclusive
        self.prefix_sum_mat = [[0 for _ in range(n)] for _ in range(m)]
        # self.prefix_sum_mat[0][0] = matrix[0][0]  # already 0
        for i in range(1, m):  # the left-most column
            self.prefix_sum_mat[i][0] = self.prefix_sum_mat[i-1][0] + matrix[i][0]
        for j in range(1, n):  # the upper-most row
            self.prefix_sum_mat[0][j] = self.prefix_sum_mat[0][j-1] + matrix[0][j]
        for i in range(1, m):
            for j in range(1, n):
                self.prefix_sum_mat[i][j] = (self.prefix_sum_mat[i-1][j] + self.prefix_sum_mat[i][j-1] 
                                             - self.prefix_sum_mat[i-1][j-1] + matrix[i][j])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        diff = 0
        if row1 > 0:
            diff -= self.prefix_sum_mat[row1-1][col2]
        if col1 > 0:
            diff -= self.prefix_sum_mat[row2][col1-1]
        if row1 > 0 and col1 > 0:
            diff += self.prefix_sum_mat[row1-1][col1-1]
        return self.prefix_sum_mat[row2][col2] + diff


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
