class Solution:
    def bestClosingTime(self, cust: str) -> int:
        
        h = m = s = 0
        for i, ch in enumerate(cust):       # [1] compute running profit where
            s += (ch == "Y") * 2 - 1        #     we add +1 for Y, -1 for N
            if s > m:                       # [2] keep track of the maximal 
                m, h = s, i+1               #     profit and its hour
        
        return h                            # [3] this is the hour with minimal penalty
