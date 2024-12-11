from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # Sort the array to process ranges in order
        nums.sort()
        max_beauty = 0
        start = 0

        # Sliding window approach
        for end in range(len(nums)):
            # Ensure the range is valid
            while nums[end] - nums[start] > 2 * k:
                start += 1
            # Update maximum beauty
            max_beauty = max(max_beauty, end - start + 1)

        return max_beauty

# Example Usage
solution = Solution()
print(solution.maximumBeauty([4, 6, 1, 2], 2))  # Output: 3
print(solution.maximumBeauty([1, 1, 1, 1], 10))  # Output: 4
