mod_ = 1_000_000_007
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:

        d = defaultdict(list)
        for i, num in enumerate(nums):
            d[num].append(i)

        ans = comb(len(d[0]), 3) %mod_
        d.pop(0)
        
        for num in d:
            twiceNum = num + num
            if twiceNum not in d: continue
            length, m = len(d[twiceNum]), 0
            for idx in d[num]:

                m = bisect_left(d[twiceNum], idx, lo = m)
                ans+= m * (length - m)
                ans%= mod_

        return ans  
