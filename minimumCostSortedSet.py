from sortedcontainers import SortedSet
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
    
        n = len(nums)
        ans = float('inf')
        total_sum = 0

        min_k = SortedSet(key=lambda x: (nums[x], x))
        rest = SortedSet(key=lambda x: (nums[x], x))

        for i in range(1, n):
            min_k.add(i)
            total_sum += nums[i]

            if len(min_k) >= k:
                removed_idx = min_k.pop()
                total_sum -= nums[removed_idx]
                rest.add(removed_idx)

            if i - dist >= 0:
                ans = min(ans, total_sum)

                to_remove = i - dist
                if to_remove in min_k:
                    min_k.remove(to_remove)
                    total_sum -= nums[to_remove]

                    if rest:
                        added_idx = rest.pop(0)
                        total_sum += nums[added_idx]
                        min_k.add(added_idx)
                else:
                    rest.remove(to_remove)

        return ans + nums[0]

