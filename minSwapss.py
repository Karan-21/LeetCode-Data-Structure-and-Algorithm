class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        arr = sorted(nums, key = lambda x: (sum(int(d) for d in str(x)), x))
        pos = {num: i for i, num in enumerate(nums)}
        visited = [False] * len(nums)
        ans = 0

        for i in range(len(nums)):
            if visited[i] or pos[arr[i]] == i:
                continue

            cycle = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pos[arr[j]]
                cycle += 1

            ans += cycle - 1

        return ans
