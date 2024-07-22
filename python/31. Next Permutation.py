class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: Find the largest index k such that nums[k] < nums[k + 1]
        k = len(nums) - 2
        while k >= 0 and nums[k] >= nums[k + 1]:
            k -= 1
        
        if k == -1:
            # If no such index exists, the array is in descending order
            nums.reverse()
            return
        
        # Step 2: Find the largest index l greater than k such that nums[k] < nums[l]
        l = len(nums) - 1
        while nums[l] <= nums[k]:
            l -= 1
        
        # Step 3: Swap the value of nums[k] with that of nums[l]
        nums[k], nums[l] = nums[l], nums[k]
        
        # Step 4: Reverse the sequence from nums[k + 1] to the end
        nums[k + 1:] = reversed(nums[k + 1:])

# Example usage:
sol = Solution()
nums = [1, 2, 3]
sol.nextPermutation(nums)
print(nums)  # Output: [1, 3, 2]

nums = [3, 2, 1]
sol.nextPermutation(nums)
print(nums)  # Output: [1, 2, 3]

nums = [1, 1, 5]
sol.nextPermutation(nums)
print(nums)  # Output: [1, 5, 1]
