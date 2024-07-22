class Solution:
    def solveSudoku(self, board):
        def is_valid(board, r, c, num):
            # Check if num is not in the current row
            for i in range(9):
                if board[r][i] == num:
                    return False
            # Check if num is not in the current column
            for i in range(9):
                if board[i][c] == num:
                    return False
            # Check if num is not in the current 3x3 sub-box
            start_row, start_col = 3 * (r // 3), 3 * (c // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False
            return True
        
        def solve(board):
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for num in '123456789':
                            if is_valid(board, r, c, num):
                                board[r][c] = num
                                if solve(board):
                                    return True
                                board[r][c] = '.'
                        return False
            return True
        
        solve(board)

# Example usage
if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    sol = Solution()
    sol.solveSudoku(board)
    for row in board:
        print(row)
