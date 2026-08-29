from collections import defaultdict


class UnionFind:
    def __init__(self, n, l):
        self.parents = list(range(n))

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            self.parents[max(x, y)] = min(x, y)
            return True
        return False


class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        pairs = sorted((num, i) for i, num in enumerate(nums))

        uf = UnionFind(n, limit)
        for i in range(n-1):
            if abs(pairs[i][0] - pairs[i+1][0]) <= limit:
                uf.union(pairs[i][1], pairs[i+1][1])

        groups = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            groups[root].append(i)

        res = [0] * n
        for indices in groups.values():
            vals = [nums[i] for i in indices]
            indices.sort()
            vals.sort()
            for i, v in zip(indices, vals):
                res[i] = v
        return res
