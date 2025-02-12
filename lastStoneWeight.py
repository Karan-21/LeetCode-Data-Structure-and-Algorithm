class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        mini = []

        for num in stones:
            heapq.heappush(mini, -num)
        
        res = 0

        while len(mini) >= 2:

            ele1 = -heapq.heappop(mini)
            ele2 = -heapq.heappop(mini)

            if ele1 == ele2:
                continue
            
            else:
                diff = abs(ele2 - ele1)
                heapq.heappush(mini, -diff)
        
        return -mini[0] if mini else 0
