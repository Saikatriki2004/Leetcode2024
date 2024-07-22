class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Initialize variables
        max_sum = nums[0]
        current_sum = nums[0]
        
        # Iterate through the array
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
    print(sol.maxSubArray([1]))  # Output: 1
    print(sol.maxSubArray([5,4,-1,7,8]))  # Output: 23
