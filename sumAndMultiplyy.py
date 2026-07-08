class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7

        pos = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        k = len(digits)

        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        prefVal = [0] * (k + 1)
        prefSum = [0] * (k + 1)

        for i in range(k):
            prefVal[i + 1] = (prefVal[i] * 10 + digits[i]) % MOD
            prefSum[i + 1] = prefSum[i] + digits[i]

        ans = []

        for l, r in queries:
            L = bisect_left(pos, l)
            R = bisect_right(pos, r) - 1

            if L > R:
                ans.append(0)
                continue

            cnt = R - L + 1

            x = (
                prefVal[R + 1]
                - prefVal[L] * pow10[cnt]
            ) % MOD

            digit_sum = prefSum[R + 1] - prefSum[L]

            ans.append((x * digit_sum) % MOD)

        return ans
