class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = mult = 0
        val = inf 
        for i in range(len(matrix)): 
            for j in range(len(matrix)):
                ans += abs(matrix[i][j])
                val = min(val, abs(matrix[i][j]))
                if matrix[i][j] < 0: mult ^= 1
        return ans - 2*mult*val
