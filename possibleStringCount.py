class Solution:
    def possibleStringCount(self, word: str) -> int:
        extras = sum(1 for i in range(1, len(word)) if word[i] == word[i - 1])
        return extras + 1
