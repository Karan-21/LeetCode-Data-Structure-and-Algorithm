class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # Keep track of the number of spells belonging to each 
        # power level
        spell_count = {}
        for p in power:
            spell_count[p] = spell_count.get(p, 0) + 1

        sorted_power = sorted(spell_count.keys())
        dp = [0] * len(sorted_power)

        for i in range(len(sorted_power)):
            prev_best = 0

            # Find the previous compatible spell and the 
            # maximum damage that could be dealt up until that level.
           
            j = i - 1
            while j >= 0 and sorted_power[j] >= sorted_power[i] - 2:
                j -= 1
            if j >= 0:
                prev_best = dp[j]

            # Calculates the most damage that could be dealt up 
            # until this point as the maximum of damage including 
            # this power level and excluding.

            dp[i] = max(prev_best + sorted_power[i] * spell_count[sorted_power[i]], dp[i-1])

        return dp[-1]
