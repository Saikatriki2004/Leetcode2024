class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])

        # Initialize a list to store the previous row's maximum points
        prev_row = points[0]
        
        # Iterate over each row starting from the second row
        for i in range(1, m):
            # Initialize two arrays to store max points from the left and right
            left = [0] * n
            right = [0] * n
            
            # Calculate max points from the left side
            left[0] = prev_row[0]
            for j in range(1, n):
                left[j] = max(left[j - 1] - 1, prev_row[j])
            
            # Calculate max points from the right side
            right[n - 1] = prev_row[n - 1]
            for j in range(n - 2, -1, -1):
                right[j] = max(right[j + 1] - 1, prev_row[j])
            
            # Update the current row based on the max of left and right arrays
            for j in range(n):
                points[i][j] += max(left[j], right[j])
            
            # Prepare for the next row
            prev_row = points[i]
        
        # The maximum value in the last row is the answer
        return max(prev_row)
sol = Solution()
print(sol.maxPoints([[1,2,3],[1,5,1],[3,1,1]]))  # Output: 9
    
