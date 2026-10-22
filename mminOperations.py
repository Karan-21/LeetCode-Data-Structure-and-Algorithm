class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        start, end = nums.index(0), nums.index(n - 1)
        distance = abs(start - end)
        if distance not in (1, n - 1):
            return -1

        step, ind, prev = 1, start, 0
        if (distance == n - 1 and end == 0) or (distance == 1 and start < end):
            step, ind, prev = -1, end, n - 1

        for _ in range(n - 2):
            ind = (ind + 1) % n
            if prev + step != nums[ind]:
                return -1    
            prev = nums[ind]

        if distance == n - 1:
            return 0 if start == 0 else 1
        
        if start < end:
            return min(start + 2, n - end + 1)
        return min(end + 1, n - start + 2)
