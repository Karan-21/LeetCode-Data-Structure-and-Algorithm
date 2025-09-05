class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        n = 0
        while True:
            diff = num1 - n * num2
            if diff <= 0:
                break
            if diff.bit_count() <= n and diff >= n:
                return n
            n += 1
        return -1
