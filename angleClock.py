class Solution:
    def angleClock(self, h: int, m: int) -> float:
        return min(abs(30*(h%12)-5.5*m),
                   360-abs(30*(h%12)-5.5*m))
