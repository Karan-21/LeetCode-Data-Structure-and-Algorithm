class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        Range = range(0, min(coins) * k + 1)
        d = defaultdict(list)

        for i in range(len(coins)):
            for comb in combinations(coins, i+1):
                d[len(comb)].append(lcm(*comb))
        
        def cnt(t, sm = 0):
            
            for coinCnt in d:
                sm+= sum(map(lambda x: (2*(key%2)-1) * (t//x), d[coinCnt]))
            return sm >= k
        
        return bisect_left(Range, True, key  = cnt)
