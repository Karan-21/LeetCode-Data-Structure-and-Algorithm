class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        ans = [0]*K + [1]*(N-K+1) + [0]*W
        val = sum(ans[K:K+W])
        for i in reversed(range(K)): 
            ans[i] = val/W
            val += ans[i] - ans[i+W]
        return ans[0]
