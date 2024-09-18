from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert all integers to strings for comparison
        nums = list(map(str, nums))
        
        # Custom comparator function to sort numbers
        def compare(x, y):
            # Compare concatenated strings in both orders
            if x + y > y + x:
                return -1  # x should come before y
            elif x + y < y + x:
                return 1  # y should come before x
            else:
                return 0  # They are equal
        
        # Sort the array using the custom comparator
        nums.sort(key=cmp_to_key(compare))
        
        # Join the sorted numbers into a single string
        largest_num = ''.join(nums)
        
        # Edge case: if the largest number is '0', return '0' instead of '000...'
        return '0' if largest_num[0] == '0' else largest_num
# Test case 1
nums = [10, 2]
print(Solution().largestNumber(nums))  # Output: "210"

# Test case 2
nums = [3, 30, 34, 5, 9]
print(Solution().largestNumber(nums))  # Output: "9534330"
