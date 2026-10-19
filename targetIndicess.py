class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        # ans = []

        # nums.sort()

        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         ans.append(i)

        # return ans

        smaller = 0
        equal = 0

        for num in nums:

            if num<target:
                smaller+=1
            elif num==target:
                equal +=1

        return list(range(smaller,smaller+equal))
        

        # smaller count gives us the count of elements smaller than target telling us about first target index

        # equal count tells us about the consecutive indices to return after first target index
