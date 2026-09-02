class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # return True
        # ....OR....
        oddCount = sum(1 for x in nums1 if x % 2 == 1)
        evenCount = len(nums1) - oddCount

        """
        # case 1 => Can we construct an all even nums2?
        # If already all even (odd_count == 0) -> yes
        # If there are odds, we need odd_count >= 2 so each odd element
        # can pick a distinct odd element to subtract (odd - odd = even)
        """
        canMakeAllEven = (oddCount == 0) or (oddCount >= 2)

        """
        # case 2 => Can we construct an all odd nums2?
        # Already all odd (even_count == 0) -> yes
        # Has evens -> needs at least one odd so evens can subtract it (even - odd = odd)
        """
        canMakeAllOdd = (oddCount >= 1)

        return canMakeAllEven or canMakeAllOdd
