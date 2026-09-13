class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        n = len(img1)

        ones1 = []
        ones2 = []

        for i in range(n):
            for j in range(n):

                if img1[i][j] == 1:
                    ones1.append((i, j))

                if img2[i][j] == 1:
                    ones2.append((i, j))

        shift_count = collections.Counter()
        max_overlap = 0

        for i1, j1 in ones1:
            for i2, j2 in ones2:

                shift = (i2 - i1, j2 - j1)

                shift_count[shift] += 1

                max_overlap = max(max_overlap, shift_count[shift])

        return max_overlap

