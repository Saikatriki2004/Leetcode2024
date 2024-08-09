#840. Magic Squares In Grid:
class Solution:
    def numMagicSquaresInside(self, grid):
        def is_magic(r, c):
            nums = set()
            for i in range(3):
                for j in range(3):
                    num = grid[r+i][c+j]
                    if num < 1 or num > 9 or num in nums:
                        return False
                    nums.add(num)
            
            # Check the sums of rows, columns, and diagonals
            return (grid[r][c] + grid[r][c+1] + grid[r][c+2] == 15 and
                    grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == 15 and
                    grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == 15 and
                    grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15 and
                    grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15 and
                    grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15 and
                    grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == 15 and
                    grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == 15)
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        # Iterate through each possible top-left corner of a 3x3 subgrid
        for r in range(rows - 2):
            for c in range(cols - 2):
                if grid[r+1][c+1] == 5 and is_magic(r, c):
                    count += 1
        
        return count
