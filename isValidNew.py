class Solution:
    def isValid(self, word: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    
        if len(word) < 3 or len(word) > 20:
            return False
    
        if any(char not in (vowels | consonants | set('0123456789')) for char in word):
            return False
    
        has_vowel = any(char in vowels for char in word)
        has_consonant = any(char in consonants for char in word)
    
        return has_vowel and has_consonant
