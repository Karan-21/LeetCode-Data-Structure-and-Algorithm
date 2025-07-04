class Solution:
    def kthCharacter(self, k: int, op: List[int]) -> str:
        # Initializing no. of moves to 0
        moves = 0
        # We add a condition for k > 1. If k == 1, it means we are at the first character,
        while k > 1: 
            # Calculate the largest power of 2 less than or equal to k using logarithm
            l = math.ceil(math.log(k, 2))
            # Subtract the largest power of 2 segment from k
            k -= 2 ** (l - 1)
            # Add the operation type from the corresponding position to the moves counter
            moves += op[l - 1]
        # Apply modulo 26 to ensure the moves wrap around within the alphabet range,
        # then convert it to a character by adding it to 'a' and using the resulting ASCII value.
        return chr(ord('a') + moves % 26)
