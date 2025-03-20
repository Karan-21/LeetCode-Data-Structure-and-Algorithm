class Solution:
    def rob(self, nums: List[int]) -> int:
        
        return max(nums[0], self.recurr(nums[1:],0,{}), self.recurr(nums[:-1],0,{}))
    
    def recurr(self,nums,idx,dp):

        if idx >= len(nums):
            return 0
        
        if idx in dp:
            return dp[idx]
        
        case1 = nums[idx] + self.recurr(nums,idx+2,dp)

        case2 = self.recurr(nums,idx+1,dp)

        dp[idx] = max(case1, case2)

        return dp[idx]
