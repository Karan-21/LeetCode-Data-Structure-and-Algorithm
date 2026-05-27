class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        state = [-1] * 26
        
        for char in word:
            if ord(char) >= 97:
                idx = ord(char) - ord('a')
                if state[idx] == -1:
                    state[idx] = 0
                elif state[idx] == 1:
                    state[idx] = 2
            else:
                idx = ord(char) - ord('A')
                if state[idx] == 0:
                    state[idx] = 1
                elif state[idx] == -1:
                    state[idx] = 2
                    
        return state.count(1)
