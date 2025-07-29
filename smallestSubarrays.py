from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:

        def update_last_seen_bits(num, index, last_seen_bits):
            """Updates the last seen indices of each bit in 'num'."""
            bit_index = 0
            while (num >> bit_index):
                if (num >> bit_index) & 1:
                    last_seen_bits[bit_index] = index
                bit_index += 1

        # Calculate the maximum bit length to cover all bits in 'nums'.
        max_bit_length = max(1, max(n.bit_length() for n in nums))

        # Initialize the last seen bits array.
        last_seen_bits = [0] * max_bit_length

        # Initialize the result array.
        result = [0] * len(nums)

        # Iterate over 'nums' in reverse order.
        for i in range(len(nums) - 1, -1, -1):
            update_last_seen_bits(nums[i], i, last_seen_bits)
            # The size of the smallest subarray with maximum bitwise OR 
            # starting at 'i' is the maximum last seen bit index - 'i' + 1.
            result[i] = max(1, max(last_seen_bits) - i + 1)

        return result
