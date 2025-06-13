
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # Sort the numbers first
        nums.sort()
        
        # Helper function to check if we can form at least p pairs with max_difference allowed
        def can_form_pairs(max_difference):
            pairs = 0
            i = 0
            while i < len(nums) - 1:
                # If we can pair nums[i] with nums[i+1]
                if nums[i + 1] - nums[i] <= max_difference:
                    pairs += 1  # We can form a pair
                    i += 2  # Move past the pair
                else:
                    i += 1  # Try the next element
            
            return pairs >= p  # We need at least p pairs

        # Binary search for the minimum possible maximum difference
        left, right = 0, nums[-1] - nums[0]
        result = right

        while left <= right:
            mid = (left + right) // 2
            if can_form_pairs(mid):
                result = mid  # We can form p pairs with this max difference
                right = mid - 1  # Try for a smaller max difference
            else:
                left = mid + 1  # Increase the max difference

        return result
