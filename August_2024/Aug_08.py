#885. Spiral Matrix III:
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int):
        # Directions are in the order: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        total_cells = rows * cols
        
        r, c = rStart, cStart  # starting point
        step = 1  # initial step length
        direction_index = 0  # start with the first direction (right)
        
        result.append([r, c])
        while len(result) < total_cells:
            for _ in range(2):  # two passes for each step length
                dr, dc = directions[direction_index]
                for _ in range(step):
                    r += dr
                    c += dc
                    # Check if within grid boundaries
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                # Change direction clockwise
                direction_index = (direction_index + 1) % 4
            # Increase step after every two directions (right and down, left and up)
            step += 1
        
        return result

# Example usage:
solution = Solution()
print(solution.spiralMatrixIII(1, 4, 0, 0))  # Output: [[0,0],[0,1],[0,2],[0,3]]
print(solution.spiralMatrixIII(5, 6, 1, 4))  # Output: [[1,4],[1,5],[2,5],...]
