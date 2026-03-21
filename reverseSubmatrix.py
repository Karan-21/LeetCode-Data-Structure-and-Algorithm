class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:

        for i in range(k // 2):
            rowA, rowB = grid[x + i], grid[x - i + k - 1]
            rowA[y: y + k], rowB[y: y + k] = rowB[y: y + k], rowA[y: y + k]

        return grid
