class Solution:
    def maxProductPath(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        Max = [[0] * n for _ in range(m)]
        Min = [[0] * n for _ in range(m)]
        Max[0][0] = A[0][0]
        Min[0][0] = A[0][0]
        for j in range(1, n):
            Max[0][j] = Max[0][j - 1] * A[0][j]
            Min[0][j] = Min[0][j - 1] * A[0][j]

        for i in range(1, m):
            Max[i][0] = Max[i - 1][0] * A[i][0]
            Min[i][0] = Min[i - 1][0] * A[i][0]
        for i in range(1, m):
            for j in range(1, n):
                if A[i][j] > 0:
                    Max[i][j] = max(Max[i - 1][j], Max[i][j - 1]) * A[i][j]
                    Min[i][j] = min(Min[i - 1][j], Min[i][j - 1]) * A[i][j]
                else:
                    Max[i][j] = min(Min[i - 1][j], Min[i][j - 1]) * A[i][j]
                    Min[i][j] = max(Max[i - 1][j], Max[i][j - 1]) * A[i][j]
        return Max[-1][-1] % int(1e9 + 7) if Max[-1][-1] >= 0 else -1
            
