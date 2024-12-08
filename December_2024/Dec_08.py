from bisect import bisect_left
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort events by their end time
        events.sort(key=lambda x: x[1])
        
        # Extract end times for binary search
        end_times = [event[1] for event in events]
        
        n = len(events)
        maxValueUntil = [0] * n
        maxValue = 0
        
        # Maintain the maximum value up to each event
        for i in range(n):
            maxValue = max(maxValue, events[i][2])
            maxValueUntil[i] = maxValue
        
        result = 0
        
        for i, (start, end, value) in enumerate(events):
            # Binary search for the latest event that ends before the current event starts
            j = bisect_left(end_times, start) - 1
            
            # Calculate the best value with this event and the previous non-overlapping event
            if j >= 0:
                result = max(result, value + maxValueUntil[j])
            else:
                result = max(result, value)
        
        return result
