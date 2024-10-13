import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Min-heap to store (value, list_index, element_index)
        min_heap = []
        max_value = float('-inf')  # Track the maximum value in the current range

        # Initialize the heap with the first element from each list
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            max_value = max(max_value, nums[i][0])

        # Initialize the smallest range with infinity
        smallest_range = [float('-inf'), float('inf')]

        # Continue until we exhaust any one list
        while min_heap:
            min_value, list_index, element_index = heapq.heappop(min_heap)

            # Update the smallest range if the current one is smaller
            if max_value - min_value < smallest_range[1] - smallest_range[0]:
                smallest_range = [min_value, max_value]

            # Move to the next element in the same list
            if element_index + 1 < len(nums[list_index]):
                next_value = nums[list_index][element_index + 1]
                heapq.heappush(min_heap, (next_value, list_index, element_index + 1))
                max_value = max(max_value, next_value)
            else:
                # If any list is exhausted, we break the loop
                break

        return smallest_range
