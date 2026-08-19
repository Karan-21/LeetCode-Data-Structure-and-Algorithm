class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = [0 for _ in range(10)]
        d = {}

        for i, j in reservedSeats:
            if i - 1 not in d:
                d[i - 1] = [j - 1]
            else:
                d[i - 1].append(j - 1)
        
        res = (n - len(d)) * 2

        for i in d:
            for k in d[i]:
                seats[k] = 1
            j = 0
            while j < 6:
                if j == 1 or j == 3 or j == 5:
                    if seats[j] == seats[j + 1] == seats[j + 2] == seats[j + 3] == 0:
                        res += 1
                        j += 3
                j += 1
            seats = [0 for _ in range(10)]
        return res
