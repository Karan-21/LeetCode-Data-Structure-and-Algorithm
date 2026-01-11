class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        # Next/Previous Smaller Element from Right and Left
        # Arr[i] < Arr[current] => Stopping Point

        # Creating an Area and Stack to return area and Stack to maintain the Max Value
        area = 0
        stack = [] # Index and Height

        # Loop through the Array using index and value
        for i,h in enumerate(heights):
            start = i

            # If we are in Increasing Order then we don't need to Pop 
            # Because We can extend it whereas if it's less than existing, we need to think
            # This Means I have found a Right Boundary
            while stack and stack[-1][1] > h:
            # So, if the Top Element on the Stack is greater than the Current Height.
                index, height = stack.pop()

                # Pop the element and calculate the area at that moment
                # To get the Width, Simply Minus the current index with the last seen
                area = max(area, height * (i - index))
                
                # Since we have seen a lower value, we need to update 
                # The start index with the current one.
                start = index
            
            stack.append((start,h))
        
        # The Stack is still not Empty
        # And the bar starts somewhere and it can be extended till End of the Array
        # Which means I CANNOT FIND THE RIGHT BOUNDARY => It can be extended to the end
        for i,h in stack:

            area = max(area, h * (len(heights) - i))

        return area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        maxi = float('-inf')

        histogram = [0] * len(matrix[0])

        for i in range(len(matrix)):

            for j in range(len(histogram)):

                if matrix[i][j] == "1":
                    histogram[j] += 1
                
                else:
                    histogram[j] = 0
            
            maxi = max(maxi, self.largestRectangleArea(histogram))
        
        return maxi










        
