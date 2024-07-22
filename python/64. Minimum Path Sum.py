class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Create the DP table with the same dimensions as grid
        dp = [[0] * n for _ in range(m)]
        
        # Initialize the top-left corner
        dp[0][0] = grid[0][0]
        
        # Initialize the first row (can only come from the left)
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # Initialize the first column (can only come from the top)
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        # Fill the rest of the DP table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        # The bottom-right cell contains the minimum path sum
        return dp[m-1][n-1]
