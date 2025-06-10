class Solution:
    def maxDifference(self, s: str) -> int:
        letterCount = Counter(s)
        odd = -1
        even = float('inf')
        for freq in letterCount.values():
            if freq % 2 == 0:
                even = min(even, freq)
            else:
                odd = max(odd, freq)
        
        return odd - even        
