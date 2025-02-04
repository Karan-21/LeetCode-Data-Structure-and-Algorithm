class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(idx, path, key):

            if key == target:
                res.append(path[:])
                return
            
            if key > target:
                return
            
            if idx >= len(nums):
                return
            
            for i in range(idx,len(nums)):

                path.append(nums[i])

                dfs(i, path, key + nums[i])

                path.pop()
        
        dfs(0,[],0)

        return res        
