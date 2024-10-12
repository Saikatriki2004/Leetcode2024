class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        
        # Mark the start and end of each interval
        for left, right in intervals:
            events.append((left, 1))    # Start of an interval
            events.append((right + 1, -1))  # End of an interval (right + 1)
        
        # Sort the events by time
        events.sort()
        
        max_groups = 0
        current_groups = 0
        
        # Traverse through events and update the current number of overlapping intervals
        for time, event in events:
            current_groups += event
            max_groups = max(max_groups, current_groups)
        
        return max_groups
