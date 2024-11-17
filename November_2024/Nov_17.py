from collections import deque
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Step 1: Create a prefix sum array
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        # Step 2: Monotonic deque to find the shortest subarray
        dq = deque()  # Will store indices
        min_length = float('inf')  # Initialize the minimum length
        
        for i in range(n + 1):
            # Step 2.1: Check if the current subarray meets the condition
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                min_length = min(min_length, i - dq.popleft())
            
            # Step 2.2: Maintain the deque in increasing order of prefix sums
            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()
            
            # Step 2.3: Add the current index to the deque
            dq.append(i)
        
        # Step 3: Return the result
        return min_length if min_length != float('inf') else -1
