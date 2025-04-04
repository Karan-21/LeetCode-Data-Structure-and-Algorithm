# https://leetcode.com/problems/triangle/solutions/2146264/c-python-simple-solution-w-explanation-recursion-dp/
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        return self.recurr(triangle, 0, 0, {})
    
    def recurr(self,nums,i,j,dp):

        if i >= len(nums):
            return 0
        
        if (i,j) in dp:
            return dp[(i,j)]
        
        case1 = nums[i][j] + self.recurr(nums, i+1, j, dp)

        case2 = nums[i][j] + self.recurr(nums, i+1, j+1, dp)

        dp[(i,j)] = min(case1, case2)

        return dp[(i,j)]
