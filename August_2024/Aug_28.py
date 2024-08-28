class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        def dfs(r, c):
            if r < 0 or r >= len(grid2) or c < 0 or c >= len(grid2[0]) or grid2[r][c] == 0:
                return True
            grid2[r][c] = 0  # Mark this cell as visited
            
            isSubIsland = True
            if grid1[r][c] == 0:
                isSubIsland = False
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if not dfs(r + dr, c + dc):
                    isSubIsland = False
            
            return isSubIsland
        
        subIslandCount = 0
        
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if grid2[r][c] == 1:
                    if dfs(r, c):
                        subIslandCount += 1
        
        return subIslandCount
solution = Solution()
grid1 = [
    [1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0]
]
grid2 = [
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1]
]
result = solution.countSubIslands(grid1, grid2)
print(result)  # Output: 2
