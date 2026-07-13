class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        res = 0

        for i in range(1,10):
            res = i
            start = i
            while res <= high and (start+1)<10:
                res = res*10+(start+1)
                if res >= low and res <= high:
                    result.append(res)
                start+=1
        
                
        return sorted(result)
