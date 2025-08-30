class Solution:
    def isValidSudoku(self, nums: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)

        for i in range(9):

            for j in range(9):

                if nums[i][j] == '.':
                    continue
                
                if (nums[i][j] in rows[i] or nums[i][j] in cols[j] or nums[i][j] in sqrs[(i//3), j//3]):
                    return False
                
                rows[i].add(nums[i][j])
                cols[j].add(nums[i][j])
                sqrs[(i//3, j//3)].add(nums[i][j]) 
        
        return True
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)

        for i in range(9):

            for j in range(9):

                if nums[i][j] == ".":
                    continue
                
                if (nums[i][j] in rows[i] or nums[i][j] in cols[j] or nums[i][j] in sqrs[(i//3), j//3]):
                    return False

                rows[i].add(nums[i][j])
                cols[j].add(nums[i][j])
                sqrs[(i//3, j//3)].add(nums[i][j]) 
        
        return True
