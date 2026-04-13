class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        # Initialize with a very large value
        abs_diff = float('inf')

        for i in range(len(nums)):
            # If we find the target value
            if nums[i] == target:
                # Calculate the absolute distance from start
                diff = abs(i - start)
                # Keep the minimum distance
                if diff < abs_diff:
                    abs_diff = min(abs_diff, diff)

        return abs_diff
