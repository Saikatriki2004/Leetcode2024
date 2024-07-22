class Solution:
    def search(self, nums: [int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Determine which part is sorted
            if nums[left] <= nums[mid]:  # Left part is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # Right part is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1  # If the target is not found

# Example usage:
solution = Solution()
print(solution.search([4,5,6,7,0,1,2], 0))  # Output: 4
print(solution.search([4,5,6,7,0,1,2], 3))  # Output: -1
print(solution.search([1], 0))              # Output: -1
