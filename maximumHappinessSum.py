class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # Sort the happiness values in non-increasing order
        happiness.sort(reverse=True)

        total = 0
        for turn in range(k):
            # Calculate the happiness contribution of the current child in this turn
            # since his happiness has been decreased for all of the past rounds
            current = max(happiness[turn] - turn, 0)
            # Accumulate the happiness contribution
            total += current
        
        return total
