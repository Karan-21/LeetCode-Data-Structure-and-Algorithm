class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)

        mini = [[grid[0][0], 0, 0]] # Cost, Row, Col

        visit = set()

        visit.add((0,0))

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while mini:

            cost, r, c = heapq.heappop(mini)

            if (r,c) == (n-1, n-1):
                return cost

            for row, col in directions:

                dr = row + r
                dc = col + c

                if 0 <= dr < n and 0 <= dc < n and (dr,dc) not in visit:

                    heapq.heappush(mini, [max(cost, grid[dr][dc]), dr, dc])

                    visit.add((dr,dc))
    
