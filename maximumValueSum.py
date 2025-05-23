class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        n = len(nums)
        diff = [0] * n
        total_sum = 0

        for i in range(n):
            diff[i] = (nums[i] ^ k) - nums[i]
            total_sum += nums[i]

        diff.sort(reverse=True)

        for i in range(0, n-1, 2):
            if diff[i] + diff[i+1] > 0:
                total_sum += diff[i] + diff[i+1]

        return total_sum
