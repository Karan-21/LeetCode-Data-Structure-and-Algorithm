class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        #Generating the values
        nums = []
        n1, num = 1, 1
        while num <= n:
            nums.append(num)
            n1 += 1
            num = n1 ** x
        
        #Using coin change logic
        def findSum(i, currentSum, memo):
            if (i, currentSum) in memo:
                return memo[(i, currentSum)]
            if currentSum == n:
                return 1
            if currentSum > n or i >= len(nums):
                return 0
            take = findSum(i+1, currentSum + nums[i], memo)
            dontTake = findSum(i+1, currentSum, memo)
            memo[(i, currentSum)] = take + dontTake
            return memo[(i, currentSum)]
                
        return findSum(0, 0, {}) % (10 ** 9 + 7)
    
