class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        total = 0
        for i in range(m):
            for j in range(n):
                total += grid[i][j]
        print(total)

        if total % 2 != 0:
            return False
        target = total // 2

        hSum = 0
        for i in range(m - 1):
            for j in range(n):
                hSum += grid[i][j]    
            if hSum == target: return True
            if hSum > target: break
        vSum = 0
        for j in range(n - 1):
            for i in range(m):
                vSum += grid[i][j]    
            if vSum == target: return True
            if vSum > target: break
        return False
