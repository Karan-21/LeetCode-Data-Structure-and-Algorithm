    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        nums.sort()

        for i, val in enumerate(nums):

            if i>0 and nums[i-1] == nums[i]:
                continue
            
            l, r = i+1, len(nums) - 1

            while l < r:

                summ = nums[l] + nums[r] + val

                if summ > 0:
                    r-=1
                
                elif summ < 0:
                    l+=1
                
                else:
                    res.append([nums[l], nums[r], val])
                    l += 1

                    while l < r and nums[l-1] == nums[l]:
                        l+=1
        
        return res
