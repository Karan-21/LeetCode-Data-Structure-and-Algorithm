class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        d=collections.defaultdict(list)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:d[(i,j)]=[[i,j-1],[i,j+1]]
                if grid[i][j]==2:d[(i,j)]=[[i-1,j],[i+1,j]]
                if grid[i][j]==3:d[(i,j)]=[[i,j-1],[i+1,j]] 
                if grid[i][j]==4:d[(i,j)]=[[i+1,j],[i,j+1]]
                if grid[i][j]==5:d[(i,j)]=[[i-1,j],[i,j-1]] 
                if grid[i][j]==6:d[(i,j)]=[[i-1,j],[i,j+1]] 

        def dfs(i,j):
            if i==len(grid)-1 and j==len(grid[0])-1:return True
            if not -1<i<len(grid) or not -1<j<len(grid[0])\
            or grid[i][j]==0:return False
            grid[i][j]=0
            for x,y in d[(i,j)]:
                if [i,j] in d[(x,y)] and dfs(x,y):return True
            return False



        return dfs(0,0)
