class Solution:
    def minimumSum(self, g: List[List[int]]) -> int:
        
        @cache
        def one(a, b, c, d):
            # same as problem 3195, just take the minimum x, y and
            # maximum x, y among all ones and calculate the final area.
            ar, br, ac, bc = inf, -inf, inf, -inf
            for i in range(a, b+1):
                for j in range(c, d+1):
                    if g[i][j]:
                        ar = min(ar, i)
                        br = max(br, i)
                        ac = min(ac, j)
                        bc = max(bc, j)
            if ar == inf:
                return 1
            return (br - ar + 1) * (bc - ac + 1)

        @cache
        def two(a, b, c, d):
            ans = float(inf)
            # cut horizontally
            for i in range(b):
                ans = min(one(a, i, c, d) + one(i + 1, b, c, d), ans)
            # cut vertically
            for j in range(d):
                ans = min(one(a, b, c, j) + one(a, b, j + 1, d), ans)
            return ans
        @cache
        def three(a, b, c, d):
            ans = float(inf)
            # cut horizontally
            for i in range(b):
                ans = min(one(a, i, c, d) + two(i + 1, b, c, d), ans)
                ans = min(two(a, i, c, d) + one(i + 1, b, c, d), ans)
            # cut vertically
            for j in range(d):
                ans = min(one(a, b, c, j) + two(a, b, j + 1, d), ans)
                ans = min(two(a, b, c, j) + one(a, b, j + 1, d), ans)
            return ans
        
        return three(0, len(g)-1, 0, len(g[0])-1)
        
