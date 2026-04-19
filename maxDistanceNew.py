class Solution:
    def maxDistance(self, nums1, nums2):

        distance = 0
        i = 0
        j = 0

        while j < len(nums2) and i < len(nums1):

            if nums1[i] <= nums2[j]:
                distance = max(distance, j - i)
                j += 1
            elif i < j:
                i += 1
            else:
                i += 1
                j += 1

        return distance
