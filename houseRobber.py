class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.solve(nums, 0, {})
    
    def solve(self,nums,idx,dp):

        if idx >= len(nums):
            return 0
        
        if idx in dp:
            return dp[idx]
        
        case1 = nums[idx] + self.solve(nums,idx+2,dp)

        case2 = self.solve(nums,idx+1,dp)

        dp[idx] = max(case1, case2)

        return dp[idx]
