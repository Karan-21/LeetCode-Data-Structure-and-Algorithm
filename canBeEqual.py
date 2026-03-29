class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        a, b, c, d = s1
        e, f, g, h = s2
        ## same a, b
        if a == e and b == f and c == g and d == h:
            return True
        ## same a, swapped b
        if a == e and b == h and c == g and d == f:
            return True
        ## swapped a, same b
        if a == g and b == f and c == e and d == h:
            return True
        ## swapped a, b
        if a == g and b == h and c == e and d == f:
            return True

        return False
