class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        def backtrack(row: int):
            if row == n:
                # All queens are placed, add the board configuration to results
                result.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if col in columns or (row - col) in pos_diagonals or (row + col) in neg_diagonals:
                    continue
                
                # Place queen
                board[row][col] = 'Q'
                columns.add(col)
                pos_diagonals.add(row - col)
                neg_diagonals.add(row + col)
                
                # Move to the next row
                backtrack(row + 1)
                
                # Remove queen
                board[row][col] = '.'
                columns.remove(col)
                pos_diagonals.remove(row - col)
                neg_diagonals.remove(row + col)
        
        result = []
        board = [['.'] * n for _ in range(n)]
        columns = set()
        pos_diagonals = set()
        neg_diagonals = set()
        
        backtrack(0)
        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.solveNQueens(4))
    # Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    print(sol.solveNQueens(1))
    # Output: [["Q"]]
