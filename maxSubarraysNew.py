class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:

        right = [[] for _ in range(n+1)]

        for a, b in conflictingPairs:
            right[max(a, b)].append(min(a, b))
        
        res = 0
        max_lefts = [0, 0]
        gain = defaultdict(int)


        for i in range(1, n+1):
            for l in right[i]:
                max_lefts.append(l)
                max_lefts.sort() # only 3 elements at max
                max_lefts.pop(0)

            res += (i - max_lefts[1])
            gain[max_lefts[1]] += (max_lefts[1] - max_lefts[0])

        return res + max(gain.values())


        
