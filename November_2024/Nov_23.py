class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        
        # Step 1: Simulate gravity for each row
        for row in box:
            # Pointer for the position where the next stone can fall
            empty_spot = len(row) - 1
            for col in range(len(row) - 1, -1, -1):
                if row[col] == '*':  # Reset empty spot after obstacle
                    empty_spot = col - 1
                elif row[col] == '#':  # Move stone to the lowest available position
                    row[col], row[empty_spot] = row[empty_spot], row[col]
                    empty_spot -= 1
        
        # Step 2: Rotate the box 90 degrees clockwise
        rotated_box = [[box[row][col] for row in range(m - 1, -1, -1)] for col in range(n)]
        
        return rotated_box
