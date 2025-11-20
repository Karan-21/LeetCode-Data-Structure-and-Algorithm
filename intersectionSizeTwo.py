class Solution:
    def intersectionSizeTwo(self, intervals):
        res, p1, p2 = 0, -float('inf'), -float('inf') # res is the result, p1 and p2 is 2 current points
        for s, e in sorted(intervals, key = lambda i: i[1]): # sort the intervals ascending by their end point
            if s > p2: res, p1, p2 = res + 2, e - 1, e
            elif p1 < s <= p2: res, p1, p2 = res + 1, p2, e
        return res
