import math

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:

        max_diagonal = 0
        max_area = 0
        
        for length, width in dimensions:
            diagonal = math.sqrt(length ** 2 + width ** 2)
            if diagonal > max_diagonal:
                max_diagonal = diagonal
                max_area = length * width
            elif diagonal == max_diagonal:
                max_area = max(max_area, length * width)
        
        return max_area
