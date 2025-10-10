class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int: # Function to find the maximum energy gain
        n = len(energy) # Get the size of the energy array
        ans = float('-inf') # Initialize a variable to store the maximum energy gain
        dp = [float('-inf')] * n # Initialize a dynamic programming array to store maximum energy gain
        dp[n - 1] = energy[n - 1] # Set the last element of dp as the energy of the last magician
        ans = max(ans, dp[n - 1]) # Update the maximum energy gained so far
        for i in range(n - 2, -1, -1): # Iterate through magicians from second last to the first
            if i + k < n: # Check if magician reachable after k jumps exists
                dp[i] = energy[i] + dp[i + k] # Calculate maximum energy gain from magician i
            else: # If magician reachable after k jumps doesn't exist
                dp[i] = energy[i] # Set maximum energy gain from magician i as its own energy
            ans = max(ans, dp[i]) # Update the maximum energy gained so far
        return ans # Return the maximum energy gained
