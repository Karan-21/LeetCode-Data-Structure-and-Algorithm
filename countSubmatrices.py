class Solution:
    def countSubmatrices(self, matrix, limit):

        rows = len(matrix)                 # number of rows
        cols = len(matrix[0])              # number of columns

        sum_mat = [[0] * (cols + 1) for _ in range(rows + 1)]  # prefix matrix
        result = 0                         # count of valid submatrices

        # build prefix sum matrix
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):

                # prefix formula
                sum_mat[r][c] = matrix[r - 1][c - 1] \
                               + sum_mat[r - 1][c] \
                               + sum_mat[r][c - 1] \
                               - sum_mat[r - 1][c - 1]

        # count valid submatrices
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):

                if sum_mat[r][c] <= limit:   # condition check
                    result += 1

        return result
