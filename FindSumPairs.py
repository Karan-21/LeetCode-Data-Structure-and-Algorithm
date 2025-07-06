from typing import List
from collections import defaultdict

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.hm = defaultdict(int)  # Frequency map for nums2

        # Build frequency map for nums2
        for num in nums2:
            self.hm[num] += 1

    def add(self, index: int, val: int) -> None:
        # Update frequency map before modifying nums2[index]
        old_val = self.nums2[index]
        self.hm[old_val] -= 1

        if self.hm[old_val] == 0:
            del self.hm[old_val]

        # Update nums2 value
        self.nums2[index] += val
        new_val = self.nums2[index]

        # Add new value to the frequency map
        self.hm[new_val] += 1

    def count(self, tot: int) -> int:
        count = 0

        # For each element in nums1, check for complements in nums2
        for num in self.nums1:
            complement = tot - num
            if complement in self.hm:
                count += self.hm[complement]
        return count

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
