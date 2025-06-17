MOD = 10**9 + 7

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        max_n = n
        # Precompute factorials and inverse factorials
        fact = [1] * (max_n)
        invfact = [1] * (max_n)

        for i in range(1, max_n):
            fact[i] = fact[i-1] * i % MOD
        
        # Fermat's Little Theorem for inverse
        invfact[max_n - 1] = pow(fact[max_n - 1], MOD - 2, MOD)
        for i in range(max_n - 2, -1, -1):
            invfact[i] = invfact[i+1] * (i+1) % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * invfact[b] % MOD * invfact[a - b] % MOD

        # Apply the formula
        choose = comb(n - 1, k)
        power = pow(m - 1, n - k - 1, MOD)
        return choose * m % MOD * power % MOD
