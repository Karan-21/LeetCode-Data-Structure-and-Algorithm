class Solution:
    def countHillValley(self, ns: List[int]) -> int:
        #Step 1
        nums = []
        l = ns[0]
        nums.append(l)
        for n in ns:
            if n != l:
                nums.append(n)
                l = n
                    
        #Step 2
        ret = 0
        for i in range (1, len(nums) - 1):
            if ((nums[i-1] < nums[i]) == (nums[i+1] < nums[i])):
                ret += 1
                
        return ret
            
