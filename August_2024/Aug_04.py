#1508. Range Sum of Sorted Subarray Sums
class Solution:
    def rangeSum(self, nums, n, left, right):
        MOD = 10**9 + 7
        
        # Step 1: Generate all subarray sums
        subarray_sums = []
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                subarray_sums.append(current_sum)
        
        # Step 2: Sort the subarray sums
        subarray_sums.sort()
        
        # Step 3: Calculate the sum from index `left` to `right` (1-indexed)
        result = sum(subarray_sums[left-1:right]) % MOD
        
        return result

# Example usage:
solution = Solution()

nums1 = [1, 2, 3, 4]
n1 = 4
left1 = 1
right1 = 5
print(solution.rangeSum(nums1, n1, left1, right1))  # Output: 13

nums2 = [1, 2, 3, 4]
n2 = 4
left2 = 3
right2 = 4
print(solution.rangeSum(nums2, n2, left2, right2))  # Output: 6

nums3 = [1, 2, 3, 4]
n3 = 4
left3 = 1
right3 = 10
print(solution.rangeSum(nums3, n3, left3, right3))  # Output: 50
