class Solution:
    def countMaxOrSubsets(self, nums):
        self.nums = nums
        self.max_or = 0

        # Calculate the maximum OR value
        for num in nums:
            self.max_or |= num
        
        # Create the tail array
        self.tail = [0] * len(nums)
        v = 0
        for i in range(len(nums) - 1, -1, -1):
            v |= nums[i]
            self.tail[i] = v
        
        # Start the recursion
        return self.recurse(0, 0)

    def recurse(self, i, partial):
        # If the current partial OR equals the max, return the count of remaining subsets
        if partial == self.max_or:
            return 1 << (len(self.nums) - i)

        # If we've reached the end of the array or it's impossible to achieve the max
        if i == len(self.nums) or (partial | self.tail[i]) != self.max_or:
            return 0

        # Recursive step: include or exclude the current element
        return self.recurse(i + 1, partial | self.nums[i]) + self.recurse(i + 1, partial)
