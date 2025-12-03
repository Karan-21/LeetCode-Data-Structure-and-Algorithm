class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        import math
        from collections import defaultdict
        def norm(dy, dx):
            if dx == 0:
                return (1, 0)
            if dy == 0:
                return (0, 1)
            g = math.gcd(dy, dx)
            dy //= g
            dx //= g
            if dx < 0:
                dy = -dy
                dx = -dx
            return (dy, dx)
        def C2(x):
            return x * (x - 1) // 2
        def C4(x):
            return x * (x - 1) * (x - 2) * (x - 3) // 24
        n = len(points)
        slopes = {}
        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                s = norm(yj - yi, xj - xi)
                if s not in slopes:
                    slopes[s] = [0, defaultdict(int)]
                slopes[s][0] += 1
                slopes[s][1][i] += 1
                slopes[s][1][j] += 1
        base_pairs = 0
        for s, (k, deg) in slopes.items():
            total = C2(k)
            share = 0
            for v in deg.values():
                share += C2(v)
            dy, dx = s
            line_cnt = {}
            for idx in deg.keys():
                x, y = points[idx]
                c = dy * x - dx * y
                line_cnt[c] = line_cnt.get(c, 0) + 1
            col = 0
            for t in line_cnt.values():
                if t >= 4:
                    col += 3 * C4(t)
            base_pairs += total - share - col
        mid_total = defaultdict(int)
        mid_dir = defaultdict(int)
        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                M = (xi + xj, yi + yj)
                s = norm(yj - yi, xj - xi)
                mid_total[M] += 1
                mid_dir[(M, s)] += 1
        sum_all = 0
        for v in mid_total.values():
            sum_all += C2(v)
        sum_same_dir = 0
        for v in mid_dir.values():
            sum_same_dir += C2(v)
        parallelograms = sum_all - sum_same_dir
        return base_pairs - parallelograms
