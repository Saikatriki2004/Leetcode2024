class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Initialize variables to track the minimum and maximum elements
        # from the arrays, and the maximum distance found so far.
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0
        
        # Iterate over the arrays starting from the second array
        for i in range(1, len(arrays)):
            # Calculate possible distances by comparing the min and max 
            # of the current array with the global max and min respectively.
            max_distance = max(max_distance, abs(arrays[i][-1] - min_val), abs(max_val - arrays[i][0]))
            
            # Update the global minimum and maximum
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        
        return max_distance

# Example usage:
sol = Solution()
print(sol.maxDistance([[1,2,3],[4,5],[1,2,3]]))  # Output: 4
print(sol.maxDistance([[1],[1]]))  # Output: 0
