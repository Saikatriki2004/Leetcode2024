from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # Pointer to place the next element which is not equal to val
        for j in range(len(nums)):  # Pointer to scan through the array
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

# Example usage:
solution = Solution()

nums1 = [3, 2, 2, 3]
val1 = 3
k1 = solution.removeElement(nums1, val1)
print(k1, nums1[:k1])  # Output: 2, [2, 2]

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
k2 = solution.removeElement(nums2, val2)
print(k2, nums2[:k2])  # Output: 5, [0, 1, 3, 0, 4]
