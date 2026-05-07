class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        prefix: list[int] = [0] * n
        mx_bound: int = 0
        for i in range(n):
            if nums[i] > mx_bound: mx_bound = nums[i]
            prefix[i] = mx_bound
        m: int = 1
        seen: list[int] = [n - 1]
        for i in range(n - 1, -1, -1):
            if nums[i] < nums[seen[-1]]:
                seen.append(i)
                m += 1
            left: int = 0
            right: int = m - 1
            while left <= right:
                middle: int = left + ((right - left) >> 1)
                if nums[seen[middle]] < prefix[i]:
                    right = middle - 1
                else: left = middle + 1
            if left < m and nums[seen[left]] < prefix[i]:
                prefix[i] = prefix[seen[left]]
        return prefix
