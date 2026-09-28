class Solution:
    def maxDepth(self, s: str) -> int:

        count = 0

        maxi = 0

        for i in s:

            if i == "(":

                count += 1

                if count > maxi:

                    maxi = count

            elif i == ")":

                count -= 1

        return maxi 
