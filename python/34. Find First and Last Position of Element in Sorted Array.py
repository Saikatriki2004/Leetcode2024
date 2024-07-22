class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        left = findLeft(nums, target)
        right = findRight(nums, target)
        
        if left <= right and left < len(nums) and nums[left] == target and nums[right] == target:
            return [left, right]
        else:
            return [-1, -1]

# Example usage:
solution = Solution()
print(solution.searchRange([5,7,7,8,8,10], 8))  # Output: [3, 4]
print(solution.searchRange([5,7,7,8,8,10], 6))  # Output: [-1, -1]
print(solution.searchRange([], 0))              # Output: [-1, -1]
