import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        
        # Build a min-heap with at most k elements
        for num in nums:
            heapq.heappush(self.min_heap, num)
            if len(self.min_heap) > k:
                heapq.heappop(self.min_heap)
    
    def add(self, val: int) -> int:
        # Add the new value to the heap
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        # The kth largest element is at the root of the min-heap
        return self.min_heap[0]

# Example usage:
# kthLargest = KthLargest(3, [4, 5, 8, 2])
# print(kthLargest.add(3))   # return 4
# print(kthLargest.add(5))   # return 5
# print(kthLargest.add(10))  # return 5
# print(kthLargest.add(9))   # return 8
# print(kthLargest.add(4))   # return 8
