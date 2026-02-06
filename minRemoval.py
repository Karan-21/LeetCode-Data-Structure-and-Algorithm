import bisect as b
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        m=0
        for i in range(n):
            a=nums[i]*k
            j=b.bisect_right(nums,a)
            m=max(m,j-i)
        return n-m
        
