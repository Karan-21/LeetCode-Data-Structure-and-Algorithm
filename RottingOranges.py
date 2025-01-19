class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh = 0

        directions = [[1,0], [-1,0], [0,-1], [0, 1]]
    
        queue = []

        m = len(grid)
        n = len(grid[0])

        for i in range(m):

            for j in range(n):

                if grid[i][j] == 1:
                    fresh += 1
                
                elif grid[i][j] == 2:
                    queue.append((i,j))
        
        time = 0

        while queue and fresh:

            for i in range(len(queue)):

                row, col = queue.pop(0)

                for r, c in directions:

                    dr = row + r
                    dc = col + c

                    if 0 <= dr < m and 0 <= dc < n and grid[dr][dc] == 1:
                        queue.append((dr,dc))
                        grid[dr][dc] = 2
                        fresh -= 1
        
            time += 1

        return time if fresh == 0 else -1
