#959. Regions Cut By Slashes:
class Solution:
    def regionsBySlashes(self, grid):
        n = len(grid)
        parent = list(range(4 * n * n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        for i in range(n):
            for j in range(n):
                root = 4 * (i * n + j)
                if grid[i][j] == '/':
                    # Top-right triangle connects to bottom-left
                    union(root + 0, root + 3)
                    union(root + 1, root + 2)
                elif grid[i][j] == '\\':
                    # Top-left triangle connects to bottom-right
                    union(root + 0, root + 1)
                    union(root + 2, root + 3)
                else:
                    # All triangles are connected in this cell
                    union(root + 0, root + 1)
                    union(root + 1, root + 2)
                    union(root + 2, root + 3)
                
                # Union with neighboring cells
                if i > 0:  # Connect to the cell above
                    union(root + 0, root - 4 * n + 2)
                if j > 0:  # Connect to the cell on the left
                    union(root + 3, root - 4 + 1)
        
        # Count distinct roots
        return sum(parent[x] == x for x in range(4 * n * n))

# Example usage:
sol = Solution()
print(sol.regionsBySlashes([" /","/ "]))  # Output: 2
print(sol.regionsBySlashes([" /","  "]))  # Output: 1
print(sol.regionsBySlashes(["/\\","\\/"]))  # Output: 5
