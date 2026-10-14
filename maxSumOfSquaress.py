class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num or sum < 1:
            return ''
        result = []
        for _ in range(num):
            digit = min(9, sum)
            result.append(str(digit))
            sum -= digit
        return ''.join(result)






        
