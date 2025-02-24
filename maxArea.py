class Solution:
    def maxArea(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1

        area = marea = 0

        while l <= r:

            if nums[l] < nums[r]:
                area = (r-l) * nums[l]
                l+=1
            
            else:
                area = (r-l) * nums[r]
                r-=1
            
            marea = max(marea, area)
        
        return marea
