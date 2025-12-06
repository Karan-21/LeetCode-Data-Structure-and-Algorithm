class Solution:
    def countPartitionsNEwChallenge(self, arr: List[int], k: int) -> int:
        n,mod=len(arr),10**9+7
        pre_sum,dp=[0]*(n+1),[0]*(n+1)
        dp[0],pre_sum[0],sl,j=1,1,SortedList(),-1
        for i in range(n):
            while sl and abs(arr[i]-sl[0][0])>k: j=max(j,sl.pop(0)[1])
            while sl and abs(arr[i]-sl[-1][0])>k: j=max(j,sl.pop()[1])
            dp[i+1]=(pre_sum[i]-pre_sum[j])%mod
            pre_sum[i+1]=(pre_sum[i]+dp[i+1])%mod
            sl.add((arr[i],i))
        return dp[n]%mod
            
            
            
            
            
            
            
            
            
            
            
            
