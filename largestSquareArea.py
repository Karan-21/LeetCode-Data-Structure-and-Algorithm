class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_side = 0
        for i in range(n):
            # any two squares comparision
                
                # Condition where we fix the boundary for the common region between two rectangles 
                # - Rect 1's bottom should be less than or equal to the Rect 2's top
                # - Rect 1's top should be greater than or equal to the Rect 2's bottom
                # Only this region will be the common area. 
                # You might think, what if there are 3 or more rectangles and their intersection is forming more area.
                # Basically 2 rectangles intersection already gives you a region as we are doing brute-force the case where the rectangle's intersection with largest region as their intersection is already covered.
                
            for j in range(i + 1, n):
                if bottomLeft[i][0] <= topRight[j][0] and bottomLeft[j][0] <= topRight[i][0] and bottomLeft[i][1] <= topRight[j][1] and bottomLeft[j][1] <= topRight[i][1]:
                    # select maximum bottom of the two to select the common square fields bottom it is always less than or equal to minimum bottom of two
                    bottom_x = max(bottomLeft[i][0], bottomLeft[j][0])
                    # select minimum top of the two to select the common square fields top as it is always less than or equal to maximum top of two
                    top_x = min(topRight[i][0], topRight[j][0])
                    # select maximum bottom of the two to select the common square fields bottom it is always less than or equal to minimum bottom of two
                    bottom_y = max(bottomLeft[i][1], bottomLeft[j][1])
                    # select minimum top of the two to select the common square fields top as it is always less than or equal to maximum top of two
                    top_y = min(topRight[i][1], topRight[j][1])
                    # difference of top_x and bottom_x gives width (imagine two vertical lines and the distance between these gives width)
                    width = top_x - bottom_x
                    # difference of top_y and bottom_y gives height (imagine two horizontal lines and the distance between these gives height)
                    height = top_y - bottom_y
                    # This side is needed because for square to be formed in a region we need both height and width to be same, so we select min of the two which indeed gives square when multiplied this minimum side by itself.
                    AtleastSide = min(width,height)
                    # compare previous max_side with current side we got from this iteration 
                    max_side = max(max_side, AtleastSide)
        return (max_side*max_side) # area of square s*s
