class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        prev = -1

        ans = []

        for i in range(len(words)):

            if groups[i] != prev:

                ans.append(words[i])

                prev = groups[i]

        return ans 
        
