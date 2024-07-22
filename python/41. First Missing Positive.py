class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # First pass: clean up the input array
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with nums[nums[i] - 1]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Second pass: find the first index with the wrong value
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all positions are correct, return n + 1
        return n + 1

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.firstMissingPositive([1, 2, 0]))  # Output: 3
    print(sol.firstMissingPositive([3, 4, -1, 1]))  # Output: 2
    print(sol.firstMissingPositive([7, 8, 9, 11, 12]))  # Output: 1
