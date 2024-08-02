class Solution:
    def minSwaps(self, nums):
        total_ones = sum(nums)
        
        if total_ones == 0:
            return 0  # If there are no 1's, no swaps needed.
        
        # Double the array to simulate circular behavior
        extended_nums = nums + nums
        
        # Initialize the sliding window
        max_ones_in_window = 0
        current_ones = 0
        
        # Sliding window on the extended array
        for i in range(len(extended_nums)):
            current_ones += extended_nums[i]
            
            if i >= total_ones:
                current_ones -= extended_nums[i - total_ones]
            
            max_ones_in_window = max(max_ones_in_window, current_ones)
        
        # The minimum swaps needed will be the total number of 1's minus the maximum 1's found in any window
        return total_ones - max_ones_in_window

# Example usage:
solution = Solution()
print(solution.minSwaps([0, 1, 0, 1, 1, 0, 0]))  # Output: 1
print(solution.minSwaps([0, 1, 1, 1, 0, 0, 1, 1, 0]))  # Output: 2
print(solution.minSwaps([1, 1, 0, 0, 1]))  # Output: 0
