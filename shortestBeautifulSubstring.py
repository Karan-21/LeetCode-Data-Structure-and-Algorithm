class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ans = ""
        i = 0
        j = 0
        c = 0

        while j < n:
            # Counting 1s
            if s[j] == '1':
                c += 1

            # If 1s Count has reached K
            if c == k:
                while i < n and c == k:
                    # Get the substring
                    s1 = s[i:j + 1]

                    # If I found a Smaller Substr -> Update
                    if not ans or len(s1) < len(ans):
                        ans = s1
                    
                    # Otherwise, get the Smallest One because Lexical Order
                    elif len(s1) == len(ans):
                        ans = min(ans, s1)
                    
                    # Found 1 -> Reduce the Counter as we are Reducing the Window
                    if s[i] == '1':
                        c -= 1

                    i += 1
            j += 1
            
        return ans
