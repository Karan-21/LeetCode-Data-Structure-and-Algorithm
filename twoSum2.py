class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}

        for i in range(len(nums)):

            if nums[i] in dict:

                return [dict[nums[i]], i]
            
            else:

                dict[target - nums[i]] = i
