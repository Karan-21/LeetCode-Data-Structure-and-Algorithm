class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maxHeap = []

        for num in nums:
            heapq.heappush(maxHeap, -num)

        ele1 = -heapq.heappop(maxHeap)
        ele2 = -heapq.heappop(maxHeap)

        return (ele1-1) * (ele2-1)
