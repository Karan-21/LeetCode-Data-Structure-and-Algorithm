class Solution(object):
    def minPairSum(self, nums):
        max_num = max(nums)
        min_num = min(nums)

        freq = [0] * (max_num - min_num + 1)

        for num in nums:
            freq[num - min_num] += 1

        left = min_num
        right = max_num
        max_pair_sum = float('-inf')

        while left <= right:
            while freq[left - min_num] > 0 and freq[right - min_num] > 0:
                pair_sum = left + right
                max_pair_sum = max(max_pair_sum, pair_sum)
                freq[left - min_num] -= 1
                freq[right - min_num] -= 1

            while freq[left - min_num] == 0 and left <= right:
                left += 1
            while freq[right - min_num] == 0 and left <= right:
                right -= 1

        return max_pair_sum
