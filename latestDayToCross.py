class DSU:
    def __init__(self, N):
        self.v = list(range(N))
        self.sizes = [1] * N

    def find(self, x):
        if self.v[x] != x:
            self.v[x] = self.find(self.v[x])
        return self.v[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            if self.sizes[px] < self.sizes[py]:  # Make px the name of the larger component
                px, py = py, px
            self.sizes[px] += self.sizes[py]
            self.v[py] = px


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        is_walkable = [[False for _ in range(col)] for _ in range(row)]

        def neighbors(r: int, c: int):
            for nr, nc in ((r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)):
                if 0 <= nr < row and 0 <= nc < col: yield nr, nc

        def xy_pair_to_index(x_co: int, y_co: int) -> int:
            return x_co * col + y_co

        N = row * col
        components = DSU(N + 2)  # 2 extra vertices

        # Connect top row to a (fake) new vertex N, and bottom row to new single vertex N+1
        for y in range(col):
            components.union(N, y)  # Top row
            components.union(N + 1, (row - 1) * col + y)  # Bottom row

        for day, (x, y) in enumerate(reversed(cells)):
            x -= 1
            y -= 1
            pair_index = xy_pair_to_index(x, y)
            is_walkable[x][y] = True
            for r, c in neighbors(x, y):
                if is_walkable[r][c]:
                    components.union(pair_index, xy_pair_to_index(r, c))

            if components.find(N) == components.find(N + 1):
                return N - 1 - day
