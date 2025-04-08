class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        res = float('inf')

        l = 0

        summ = 0

        for r in range(len(nums)):

            summ += nums[r]

            while summ >= target:
                res = min(res, r - l + 1)
                summ -= nums[l]
                l+=1
        
        return res if res != float('inf') else 0
            
            

            
