class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ps = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
        res = 0
        for i in range(m):
            for j in range(n):
                ps[i + 1][j + 1][0] = ps[i][j + 1][0] + ps[i + 1][j][0] - ps[i][j][0]
                ps[i + 1][j + 1][1] = max(ps[i][j + 1][1], ps[i + 1][j][1])
                if grid[i][j] == "X": 
                    ps[i + 1][j + 1][0] += 1
                    ps[i + 1][j + 1][1] = 1
                if grid[i][j] == "Y": ps[i + 1][j + 1][0] -= 1
                if ps[i + 1][j + 1][1] and ps[i + 1][j + 1][0] == 0: res += 1
        return res
