class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        nums = ''
        for i in range(len(s) - 1, -1, -1): # read from right 
            nums = s[i] + nums 
            if int(nums, base = 2) > k: # until it makes larger k
				# Add all zeros as leading zeros and add the size of the current valid nums
                return s[:i].count('0') + len(nums) - 1 # we added the digit that makes it > k, - 1 to remove such digit.
        return len(s)
