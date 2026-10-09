class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        need = 0

        for c in s:
            if c == '(':
                need += 2

                # If need is odd, insert one ')' before this '('
                if need % 2 == 1:
                    ans += 1
                    need -= 1

            else:
                need -= 1

                # No opening parenthesis available to match ')'
                if need < 0:
                    ans += 1  # Insert '('
                    need = 1  # One more ')' is still required

        return ans + need
