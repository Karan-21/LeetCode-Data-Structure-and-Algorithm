class Solution:
    def lenOfVDiagonal(self, g: List[List[int]]) -> int:
        n, m = len(g), len(g[0])
        D = [(-1, 1), (1, 1), (1, -1), (-1, -1)] 
        inb = lambda i, j: 0 <= i < n and 0 <= j < m
        res = 0

        dp0 = [[[0]*m for _ in range(n)] for _ in range(4)] 
        dp2 = [[[0]*m for _ in range(n)] for _ in range(4)] 
        for d, (dr, dc) in enumerate(D):
            rows = range(n-1, -1, -1) if dr >= 0 else range(n)
            cols = range(m-1, -1, -1) if dc >= 0 else range(m)
            for i in rows:
                for j in cols:
                    ni, nj = i + dr, j + dc
                    if g[i][j] == 0: dp0[d][i][j] = 1 + (dp2[d][ni][nj] if inb(ni, nj) else 0)
                    if g[i][j] == 2: dp2[d][i][j] = 1 + (dp0[d][ni][nj] if inb(ni, nj) else 0)

        for d, (dr, dc) in enumerate(D):
            t = (d + 1) % 4  
            for i in range(n):
                for j in range(m):
                    if g[i][j] != 1: 
                        continue
                    r, c, need, L = i, j, 1, 0
                    while inb(r, c) and g[r][c] == need:
                        L += 1
                        res = max(res, L) 
                        tr, tc = r + D[t][0], c + D[t][1]
                        if inb(tr, tc):  
                            res = max(res, L + (dp2[t][tr][tc] if L & 1 else dp0[t][tr][tc]))
                        r, c = r + dr, c + dc
                        need = 2 if need == 1 else (0 if need == 2 else 2)

        return res
