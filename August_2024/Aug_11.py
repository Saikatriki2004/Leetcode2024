class Solution:
    
    def minDays(self, grid):
        def isConnected(grid):
            # Use DFS to check if the grid is connected
            def dfs(r, c):
                if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                    return
                grid[r][c] = 0  # Mark this cell as visited
                for dr, dc in directions:
                    dfs(r + dr, c + dc)
            
            count = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        count += 1
                        if count > 1:
                            return False  # More than one island
                        dfs(i, j)
            return count == 1  # Exactly one island

        # Check if grid is initially connected
        def checkIsConnected():
            # Make a deep copy of the grid and check
            copy_grid = [row[:] for row in grid]
            return isConnected(copy_grid)
        
        # Direction vectors for exploring neighbors
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        
        # Base case: check if grid is already disconnected
        if not checkIsConnected():
            return 0
        
        # Try removing each land cell and check if the grid gets disconnected
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0  # Remove the cell
                    if not checkIsConnected():
                        return 1  # Found a way to disconnect the grid in one move
                    grid[i][j] = 1  # Restore the cell
        
        return 2  # If no single cell removal disconnects the grid, it will take at least 2 days

# Example usage:
sol = Solution()
print(sol.minDays([[0,1,1,0],[0,1,1,0],[0,0,0,0]]))  # Output: 2
print(sol.minDays([[1,1]]))  # Output: 2
