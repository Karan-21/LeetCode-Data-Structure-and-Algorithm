from collections import deque
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # Maintain a queue of sorted queries based on l from [l,r]
        q= deque(sorted(queries))
        # list to maintain max heap
        h = []
        selected =[]
        ans = 0
        # print(q)
        for i in range(len(nums)):
            # First pull out those queries for which l <= i 
            # and put it's r into max-heap
            while q and q[0][0] <= i:
                heapq.heappush(h,-q.popleft()[1])

            # Before consideration, remove those r's from
            # selected array which are less than i ( outside the range)
            while selected and selected[0]<i:
                heapq.heappop(selected)
            
            # the number of r's in selected are now greater
            # than i, signifying possibility of using those

            # Now you can select the largest r's from max-heap
            # to be put into selected, in the middle if we find ineligible
            # r, return -1
            while nums[i] > len(selected):
                if h and -h[0] >= i:
                    # print(-h[0],i)
                    heapq.heappush(selected,-heapq.heappop(h))
                    
                    ans += 1
                else:
                    return -1
        # ans represents minimum number of queries
        return len(queries)-ans

        
