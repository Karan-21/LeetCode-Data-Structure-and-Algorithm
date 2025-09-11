class Solution:    
    def sortVowels(self, s: str) -> str:
        s, vowels, positions, vowSet = list(s), [], [], set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    
        for i, c in enumerate(s):
            if c in vowSet:
                vowels.append(c)
                positions.append(i)
        
        vowels.sort()

        for i, c in zip(positions, vowels):
            s[i] = c
        
        return ''.join(s)
