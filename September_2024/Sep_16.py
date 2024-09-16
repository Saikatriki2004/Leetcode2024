class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Function to convert time "HH:MM" into minutes from 00:00
        def convertToMinutes(time: str) -> int:
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes
        
        # Convert all time points into minutes
        minutes_list = [convertToMinutes(time) for time in timePoints]
        
        # Sort the time points by their minute values
        minutes_list.sort()
        
        # Initialize the minimum difference with a large value
        min_diff = float('inf')
        
        # Compare consecutive time points
        for i in range(1, len(minutes_list)):
            min_diff = min(min_diff, minutes_list[i] - minutes_list[i - 1])
        
        # Also consider the difference between the last and the first time point (circular comparison)
        # For circular comparison, we wrap around by adding 1440 (24*60) to the first time point
        min_diff = min(min_diff, 1440 + minutes_list[0] - minutes_list[-1])
        
        return min_diff

# Example usage:
sol = Solution()
print(sol.findMinDifference(["23:59", "00:00"]))  # Output: 1
print(sol.findMinDifference(["12:01", "00:00", "23:59"]))  # Output: 1
