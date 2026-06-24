class Solution:
    MOD = 10**9 + 7

    def dot(self, a: list[int], b: list[int]) -> int:
        return sum(x * y for x, y in zip(a, b)) % self.MOD

    def trans(self, a: list[list[int]]) -> None:
        n = len(a)
        for i in range(n):
            for j in range(i + 1, n):
                a[i][j], a[j][i] = a[j][i], a[i][j]

    def mul(self, a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
        n = len(a)
        self.trans(b)
        return [[self.dot(a[i], b[j]) for j in range(n)] for i in range(n)]

    def binexp(self, a: list[list[int]], p: int) -> list[list[int]]:
        n = len(a)
        res = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        while p:
            if p & 1:
                res = self.mul(res, a)
            a = self.mul(a, a)
            p >>= 1
        return res

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        e = [[1 if j > i else 0 for j in range(m)] for i in range(m)]
        o = [[e[m - 1 - i][m - 1 - j] for j in range(m)] for i in range(m)]

        conj = self.mul(e, o)
        dist = n - 1

        if dist % 2 == 1:
            conj = self.binexp(conj, dist // 2)
            conj = self.mul(conj, e)
        else:
            conj = self.binexp(conj, dist // 2)

        base = [1] * m
        ans = sum(self.dot(row, base) for row in conj) % self.MOD
        return (ans * 2) % self.MOD
