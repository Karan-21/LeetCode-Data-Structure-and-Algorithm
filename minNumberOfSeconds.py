class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        heap = [(time, time, 1) for time in workerTimes]
        heapify(heap)

        while mountainHeight > 1:
            totalTime, originalTime, multiplier = heap[0]
            newMultiplier = multiplier + 1
            newTotalTime = originalTime * ((newMultiplier * (newMultiplier + 1)) // 2)
            heapreplace(heap, (newTotalTime, originalTime, newMultiplier))
            mountainHeight -= 1
        return heappop(heap)[0]
