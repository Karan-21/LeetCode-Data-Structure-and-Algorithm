class Solution:
    def pacificAtlantic(self, nums: List[List[int]]) -> List[List[int]]:
        
        m = len(nums)
        n = len(nums[0])

        pac = set()
        atl = set()

        def dfs(i,j,visit,prev):

            if i<0 or j<0 or i==m or j==n or (i,j) in visit or nums[i][j] < prev:
                return
            
            visit.add((i,j))

            dfs(i+1,j,visit,nums[i][j])
            dfs(i-1,j,visit,nums[i][j])
            dfs(i,j+1,visit,nums[i][j])
            dfs(i,j-1,visit,nums[i][j])
        
        for i in range(n):
            dfs(0,i,pac,nums[0][i])
            dfs(m-1,i,atl,nums[m-1][i])
        
        for i in range(m):
            dfs(i,0,pac,nums[i][0])
            dfs(i,n-1,atl,nums[i][n-1])
        
        res = []

        for i in range(m):
            for j in range(n):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])

        return res
