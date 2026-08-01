class Solution:
    def solve(self, i, j, nums):
        if i == j:
            return nums[i]

        takeLeft = nums[i] - self.solve(i + 1, j, nums)
        takeRight = nums[j] - self.solve(i, j - 1, nums)

        return max(takeLeft, takeRight)

    def PredictTheWinner(self, nums):
        return self.solve(0, len(nums) - 1, nums) >= 0
