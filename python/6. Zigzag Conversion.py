class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: If numRows is 1, return the original string
        if numRows == 1:
            return s
        
        # Initialize a list of strings for each row
        rows = [''] * min(numRows, len(s))
        
        # Initialize variables to track the current row and direction
        cur_row = 0
        going_down = False
        
        # Iterate over each character in the string
        for char in s:
            rows[cur_row] += char
            
            # Determine whether to go down or up
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            
            # Update the current row
            cur_row += 1 if going_down else -1
        
        # Combine all rows into one string
        return ''.join(rows)
