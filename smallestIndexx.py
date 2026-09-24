class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            num = nums[i]
            digitSum = 0
            while num > 0:
                digitSum+= (num % 10)
                num//=10
            if digitSum == i:
                return i
        return -1
