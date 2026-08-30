class Solution:
    def minimumDeletions(self, nums):
        minIndex = 0
        maxIndex = 0
        n = len(nums)

        for i in range(n):
            if nums[i] < nums[minIndex]:
                minIndex = i
            if nums[i] > nums[maxIndex]:
                maxIndex = i

        left = min(minIndex, maxIndex)
        right = max(minIndex, maxIndex)
        a = left + 1 + (n - right)

        return min(right + 1, min(n - left, a))
