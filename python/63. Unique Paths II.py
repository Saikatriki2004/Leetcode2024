class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # If the starting or ending cell is an obstacle, return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        # Create the DP table
        dp = [[0] * n for _ in range(m)]
        
        # Initialize the starting cell
        dp[0][0] = 1
        
        # Fill the DP table
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0  # Obstacle cell
                else:
                    if i > 0:
                        dp[i][j] += dp[i-1][j]  # Add paths from above
                    if j > 0:
                        dp[i][j] += dp[i][j-1]  # Add paths from the left
        
        # The bottom-right corner has the answer
        return dp[m-1][n-1]
