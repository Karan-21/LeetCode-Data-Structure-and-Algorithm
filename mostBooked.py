class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        avail = [i for i in range(n)]

        used = [] # End, Room

        count = [0] * n

        meetings.sort()

        for start, end in meetings:

            while used and used[0][0] <= start:
                endT, room = heapq.heappop(used)
                heapq.heappush(avail, room)
            
            if not avail:
                endT, room = heapq.heappop(used)
                end = endT + (end - start)
                heapq.heappush(avail, room)
            
            room = heapq.heappop(avail)
            heapq.heappush(used, (end, room))

            count[room] += 1

        return count.index(max(count))
