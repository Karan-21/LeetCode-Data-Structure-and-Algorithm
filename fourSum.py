class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()

        res = set()

        for i in range(len(nums)):

            for j in range(i+1, len(nums)):

                l, r = j+1, len(nums) - 1

                while l < r:

                    summ = nums[l] + nums[r] + nums[i] + nums[j]

                    if summ == target:
                        res.add((nums[l], nums[r], nums[i], nums[j]))
                        l+=1
                        r-=1
                    
                    elif summ < target:
                        l += 1
                    
                    else:
                        r -= 1
        
        return res
