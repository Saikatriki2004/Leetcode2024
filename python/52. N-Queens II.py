class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row: int):
            if row == n:
                # A valid configuration is found
                nonlocal count
                count += 1
                return
            
            for col in range(n):
                if col in columns or (row - col) in pos_diagonals or (row + col) in neg_diagonals:
                    continue
                
                # Place queen
                columns.add(col)
                pos_diagonals.add(row - col)
                neg_diagonals.add(row + col)
                
                # Move to the next row
                backtrack(row + 1)
                
                # Remove queen
                columns.remove(col)
                pos_diagonals.remove(row - col)
                neg_diagonals.remove(row + col)
        
        count = 0
        columns = set()
        pos_diagonals = set()
        neg_diagonals = set()
        
        backtrack(0)
        return count

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.totalNQueens(4))  # Output: 2
    print(sol.totalNQueens(1))  # Output: 1
