class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        n=len(grid)
        m=len(grid[0])
        temp=deque()
        for i in range(n):
            for j in range(m):
                temp.append(grid[i][j])
                
        temp.rotate(k)
        k=0
        
        for i in range(n):
            for j in range(m):
                grid[i][j]=temp[k]
                k+=1
        
        return grid
