class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        res = []

        for inter in intervals:

            if res == [] or res[-1][1] < inter[0]:
                res.append(inter)
            
            else:
                res[-1][1] = max(res[-1][1], inter[1])
        
        return res
