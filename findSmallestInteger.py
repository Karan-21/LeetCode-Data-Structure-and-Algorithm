class Solution:
    def findSmallestInteger(self, nums: List[int], val: int) -> int:
        nums = sorted( [i % val for i in nums] )
        seen = set(nums)
        t = 1
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                seen.add(nums[i] + (t * val))
                t += 1
            else:
                t = 1
        
        for i in range(len(seen) + 1):
            if i not in seen:
                return i
