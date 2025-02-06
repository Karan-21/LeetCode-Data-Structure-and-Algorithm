class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        res = []

        def dfs(idx, path):

            res.append(path[:])

            for i in range(idx,len(nums)):

                if i != idx and nums[i] == nums[i-1]:
                    continue
                
                path.append(nums[i])

                dfs(i+1,path)

                path.pop()

        
        dfs(0,[])

        return res
