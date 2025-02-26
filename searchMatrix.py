class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:

        m = len(nums)
        n = len(nums[0])

        l = 0
        r = (m*n) - 1

        while l <= r:

            mid = (l+r) // 2

            row = mid // n
            col = mid % n

            if nums[row][col] == target:
                return True
            
            elif nums[row][col] < target:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return False
