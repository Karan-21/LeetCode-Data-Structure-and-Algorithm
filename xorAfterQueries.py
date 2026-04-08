class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for query in queries:
            l, r, k, v = query[0], query[1], query[2], query[3]
            while l <= r:
                nums[l] = (nums[l] * v) % (10**9 + 7)
                l += k

        res = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            xor = 0
            i = 0
            while num > 0 or res > 0:
                if (num % 2 == 1 and res % 2 == 0) or (num % 2 == 0 and res % 2 == 1):
                    xor += 2**i
                num >>= 1
                res >>= 1
                i += 1

            res = xor
        
        return res
