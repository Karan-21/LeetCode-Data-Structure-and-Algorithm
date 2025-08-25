class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        m = len(nums)
        n = len(nums[0])

        upward = True

        res = []

        i = j = 0

        while len(res) != (m*n):

            if upward:

                while i >= 0 and j < n:
                    res.append(nums[i][j])
                    i -=1
                    j+=1

                if j == n:
                    j -= 1
                    i += 2

                else:
                    i += 1

                upward = False

            else:

                while i < m and j >= 0:
                    res.append(nums[i][j])
                    i+=1
                    j-=1

                if i == m:
                    j += 2
                    i -= 1

                else:
                    j += 1

                upward = True

        return res







