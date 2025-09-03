class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : (-x[1],x[0]))
        ans = 0
        for i in range(len(points)):
            x = inf
            for j in range(i+1, len(points)):
                if points[j][0] < points[i][0] or x < points[i][0]:
                    continue
                if points[j][0] < x:
                    ans += 1
                x = min(points[j][0],x)
                
        return ans
