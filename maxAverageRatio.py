import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        total = sum(p / t for p, t in classes)
        heap = [(p / t - (p + 1) / (t + 1), p, t) for p, t in classes]
        heapq.heapify(heap)
        for _ in range(extraStudents):
            increase, p, t = heapq.heappop(heap)
            total -= increase
            p, t = p + 1, t + 1
            heapq.heappush(heap, ((p / t - (p + 1) / (t + 1), p, t)))
        return total / len(classes)
