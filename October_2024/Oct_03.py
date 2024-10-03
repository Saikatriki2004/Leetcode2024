class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        target = total_sum % p
        
        # If the total sum is already divisible by p, return 0
        if target == 0:
            return 0
        
        # Dictionary to store the prefix sum modulo p and its index
        prefix_mod = {0: -1}  # Handle case where the valid subarray starts at index 0
        prefix_sum = 0
        min_length = float('inf')
        
        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            # Find the prefix that matches the required remainder to remove
            desired_prefix = (prefix_sum - target) % p
            if desired_prefix in prefix_mod:
                min_length = min(min_length, i - prefix_mod[desired_prefix])
            
            # Update the prefix_mod dictionary with the current prefix_sum
            prefix_mod[prefix_sum] = i
        
        # If min_length is still inf, no valid subarray was found
        return min_length if min_length != float('inf') and min_length != len(nums) else -1

# Example usage:
solution = Solution()
print(solution.minSubarray([3,1,4,2], 6))  # Output: 1
print(solution.minSubarray([6,3,5,2], 9))  # Output: 2
print(solution.minSubarray([1,2,3], 3))    # Output: 0
print(solution.minSubarray([1,2,3], 7))    # Output: -1
