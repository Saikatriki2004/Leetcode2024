from collections import Counter

class Solution:
    def canBeEqual(self, target, arr):
        # Check if both arrays have the same frequency of elements
        return Counter(target) == Counter(arr)

# Example usage:
solution = Solution()

target1 = [1, 2, 3, 4]
arr1 = [2, 4, 1, 3]
print(solution.canBeEqual(target1, arr1))  # Output: True

target2 = [7]
arr2 = [7]
print(solution.canBeEqual(target2, arr2))  # Output: True

target3 = [3, 7, 9]
arr3 = [3, 7, 11]
print(solution.canBeEqual(target3, arr3))  # Output: False
