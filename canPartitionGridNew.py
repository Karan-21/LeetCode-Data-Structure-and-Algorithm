class Solution:
    def canPartitionGridNew(self, grid):
        m, n = len(grid), len(grid[0])
        total = 0
        
        for row in grid:
            for num in row:
                total += num
        
        #Handle for m==1 and n==1 separately as i was getting wrong answer for it
        if m == 1:
            left = 0
            for i in range(n):
                for j in range(m):
                    left += grid[j][i]
                right = total - left
                if left > right:
                    if (left - right) == grid[0][0]:
                        return True
                elif right > left:
                    if (right - left) == grid[0][n - 1]:
                        return True
                else:
                    return True
            #if n==3 then our logic of removing only border element doesnt apply as the elements can be divided in 2 parts even if we remove middle element
            if n == 3:
                if grid[0][0] == grid[m - 1][n - 1]:
                    return True
            return False
        
        #similar logic to m==1 just swap m and n
        if n == 1:
            left = 0
            for i in range(m):
                for j in range(n):
                    left += grid[i][j]
                right = total - left
                if left > right:
                    if (left - right) == grid[0][0]:
                        return True
                elif right > left:
                    if (right - left) == grid[m - 1][0]:
                        return True
                else:
                    return True
            if m == 3:
                if grid[0][0] == grid[m - 1][n - 1]:
                    return True
            return False
        
        # Add all border elements for row and column separately
        rowallhs, colallhs = {}, {}
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1:
                    rowallhs[grid[i][j]] = rowallhs.get(grid[i][j], 0) + 1
                if j == 0 or j == n - 1:
                    colallhs[grid[i][j]] = colallhs.get(grid[i][j], 0) + 1
        
        # maintain the frequency of border elements of row and column till current row and column respectively
        rowhs, colhs = {}, {}
        
        top = 0
        for i in range(m):
            for j in range(n):
                #if element is on border of column, add it in hashset
                if j == 0 or j == n - 1:
                    rowhs[grid[i][j]] = rowhs.get(grid[i][j], 0) + 1
                top += grid[i][j]
            
            bottom = total - top
            
            if top == bottom:
                return True
            
            if top > bottom:
                #if top>bottom then we have to remove an element from top if it exists,if the difference exists then we can remove it and get equal sum
                diff = top - bottom
                if diff in rowhs:
                    return True
            elif bottom > top:
                #if bottom>top then we have to remove an element from bottom,but we have only maintained elements of top,here rowallhs comes into play
                diff = bottom - top
                #in if block we will heck that if the elements is present in hashmap of all border elements for columns and if it is not present in rowhs(currently encountered elements in upper array), then the difference exists in bottom part and we can equalize the sum by removing it
                if diff in colallhs and diff not in rowhs:
                    return True
                elif diff in colallhs and diff in rowhs and (colallhs[diff] - rowhs[diff] >= 1):
                    return True
        
        left = 0
        # same explanation but for rows
        for j in range(n):
            for i in range(m):
                if i == 0 or i == m - 1:
                    colhs[grid[i][j]] = colhs.get(grid[i][j], 0) + 1
                left += grid[i][j]
            
            right = total - left
            
            if left == right:
                return True
            
            if left > right:
                diff = left - right
                if diff in colhs:
                    return True
            elif right > left:
                diff = right - left
                if diff in rowallhs and diff not in colhs:
                    return True
                elif diff in rowallhs and diff in colhs and (rowallhs[diff] - colhs[diff]) != 0:
                    return True
        
        return False
    
