class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(x):
            visited.add(x)
            for y in row_map[stones[x][0]]:
                if y not in visited:
                    dfs(y)
            for y in col_map[stones[x][1]]:
                if y not in visited:
                    dfs(y)

        row_map = {}
        col_map = {}

        # Create mappings of rows and columns to their respective stones
        for i, (row, col) in enumerate(stones):
            if row not in row_map:
                row_map[row] = []
            row_map[row].append(i)
            
            if col not in col_map:
                col_map[col] = []
            col_map[col].append(i)

        visited = set()
        num_islands = 0

        for i in range(len(stones)):
            if i not in visited:
                dfs(i)
                num_islands += 1

        return len(stones) - num_islands
