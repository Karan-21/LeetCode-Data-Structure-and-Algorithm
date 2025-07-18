class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        
        L = len(nums)
        N = L // 3
        
        import heapq as hq
        
        # calculate sum_first of different borders
        first = [-n for n in nums[:N]] # negative symbol for max heap
        hq.heapify(first)
        curr_sum = sum(nums[:N])
        sum_firsts = {N: curr_sum}
        for i in range(N, L):
            hq.heappush(first, -nums[i])
            curr_sum += nums[i] + hq.heappop(first) # substract negative = add positive
            sum_firsts[i+1] = curr_sum
        
        
        # calculate sum_second of different borders
        second = [n for n in nums[-N:]]
        hq.heapify(second)
        curr_sum = sum(nums[-N:])
        sum_seconds = {2 * N : curr_sum}
        for i in range(2*N-1, -1, -1):
            hq.heappush(second, nums[i])
            curr_sum += nums[i] - hq.heappop(second)
            sum_seconds[i] = curr_sum
        
        # calculate diff for every border
        ans = math.inf
        for i in range(N, N * 2 + 1):
            ans = min(ans, sum_firsts[i] - sum_seconds[i])
        
        
        return ans     
