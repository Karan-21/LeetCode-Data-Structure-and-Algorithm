class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 1000000007
        P = ['ryr', 'yry', 'gry', 'ryg', 'yrg', 'grg', 'rgr', 'ygr', 'gyr', 'rgy', 'ygy', 'gyg']
        nei = [[i for i, x in enumerate(P) if all(a != b for a, b in zip(x, p))] for p in P]
        
        dp = [1] * 12
        for i in range(n - 1):
            dp = [sum(dp[j] for j in nei[i]) % MOD for i in range(12)]
        return sum(dp) % MOD
