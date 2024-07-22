class Solution:
    def isValidSudoku(self, board):
        # Initialize sets for rows, columns, and 3x3 sub-boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell != '.':
                    # Check if the digit already exists in the corresponding row, column or box
                    if (cell in rows[r] or
                        cell in cols[c] or
                        cell in boxes[(r // 3) * 3 + (c // 3)]):
                        return False
                    # Add the digit to the corresponding row, column and box sets
                    rows[r].add(cell)
                    cols[c].add(cell)
                    boxes[(r // 3) * 3 + (c // 3)].add(cell)
        
        return True
