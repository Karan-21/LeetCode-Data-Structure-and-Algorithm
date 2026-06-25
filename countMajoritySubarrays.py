class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        balance = n + 1

        freq = [0] * (2 * n + 2)
        pref = [0] * (2 * n + 2)

        freq[balance] = 1
        pref[balance] = 1

        answer = 0

        for num in nums:
            if num == target:
                balance += 1
            else:
                balance -= 1

            freq[balance] += 1
            pref[balance] = pref[balance - 1] + freq[balance]

            answer += pref[balance - 1]

        return answer
