class Solution:
    def rotate(self, nums: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(nums)

        for i in range(n):
            for j in range(i,n):
                nums[i][j], nums[j][i] = nums[j][i], nums[i][j]
        
        for i in range(n):
            nums[i].reverse()

