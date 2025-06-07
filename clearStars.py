class Solution:
    def clearStars(self, s: str) -> str:
        s = list(s)
        pq = []
        for i, ch in enumerate(s): 
            if ch == '*': s[-heappop(pq)[1]] = '*'
            else: heappush(pq, (ch, -i))
        return ''.join(s).replace('*', '')
