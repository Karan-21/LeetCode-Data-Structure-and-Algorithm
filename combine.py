class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        comb = []

        def backtrack(start):
            if len(comb) == k:
                result.append(comb[:])
                return
            
            for num in range(start, n + 1):
                comb.append(num)
                backtrack(num + 1)
                comb.pop()

        backtrack(1)
        return result
