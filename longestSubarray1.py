# https://www.youtube.com/watch?v=SQ8tY9nxeZU
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        res = 0
        i = 0
        j = 0
        zeroIdx = -1

        while j < len(nums):

            if nums[j] == 0:

                i = zeroIdx + 1
                zeroIdx = j

            res = max(res, j-i)

            j+=1
        
        return res
