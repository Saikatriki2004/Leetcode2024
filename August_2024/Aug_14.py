from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        def count_pairs_with_distance_less_equal(mid):
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count
        
        low = 0
        high = nums[-1] - nums[0]
        
        while low < high:
            mid = (low + high) // 2
            if count_pairs_with_distance_less_equal(mid) < k:
                low = mid + 1
            else:
                high = mid
        
        return low
      
  # Example usage:
  sol = Solution()
  print(sol.smallestDistancePair([1, 3, 1], 1))  # Output: 0
  print(sol.smallestDistancePair([1, 1, 1], 2))  # Output: 0
  print(sol.smallestDistancePair([1, 6, 1], 3))  # Output: 5
