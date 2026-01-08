class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        def solve(i,j,flag):
            if i==len(nums1) or j==len(nums2):
                return 0 if flag else -1
            if dp[i][j][flag]!=-1:return dp[i][j][flag]
            notpick=max(solve(i+1,j,flag),solve(i,j+1,flag))
            pick=nums1[i]*nums2[j]+solve(i+1,j+1,1)
            dp[i][j][flag]=max(pick,notpick)
            return dp[i][j][flag]
        dp=[[[-1 for k in range(2)]for j in range(len(nums2))]for i in range(len(nums1))]
        print(dp)
        ans=solve(0,0,False)
        if ans==-1:return max(min(nums1)*max(nums2),max(nums1)*min(nums2))
        return ans
