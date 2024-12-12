import heapq
from math import sqrt, floor
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Convert gifts to a max-heap by pushing negative values
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)

        # Perform the operations for k seconds
        for _ in range(k):
            # Extract the largest pile (negated)
            max_gift = -heapq.heappop(max_heap)
            # Calculate remaining gifts in the pile
            remaining = floor(sqrt(max_gift))
            # Push the remaining gifts back into the heap (negated)
            heapq.heappush(max_heap, -remaining)

        # Sum up the remaining gifts
        return -sum(max_heap)

# Example Usage
solution = Solution()
print(solution.pickGifts([25, 64, 9, 4, 100], 4))  # Output: 29
print(solution.pickGifts([1, 1, 1, 1], 4))         # Output: 4
