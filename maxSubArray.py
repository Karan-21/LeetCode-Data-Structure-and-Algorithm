class Solution(object):
    def maxSubArray(self, nums):

        # Assuming -inf element is the Maximum initally
        maxi = float('-inf')

        # Summ variable for maintaining the Sum
        summ = 0

        for i in nums:

            # Calculate the ongoing summ
            summ += i
            
            # Maintain the Maxi Summ at the same time
            maxi = max(maxi, summ)

            # At any point if the Sum becomes Less than 0
            if summ < 0:
                # Reset it to 0 because we don't need negative sum
                summ = 0
        
        return maxi
