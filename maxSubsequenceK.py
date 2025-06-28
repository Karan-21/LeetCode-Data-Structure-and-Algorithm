class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:

        maxHeap = []

        for i in range(len(nums)):
            heapq.heappush(maxHeap, [-nums[i], i])

        res = []

        while k > 0:

            temp = heapq.heappop(maxHeap)
            
            ele, idx = -temp[0], temp[1]

            res.append([idx,ele])

            k -= 1

        return [val for i,val in sorted(res)]
