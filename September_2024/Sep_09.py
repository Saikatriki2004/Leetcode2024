# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Initialize matrix with -1
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        
        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_direction = 0  # Start by moving right
        
        row, col = 0, 0  # Start at top-left corner
        top_bound, bottom_bound = 0, m - 1
        left_bound, right_bound = 0, n - 1
        
        current = head  # Pointer to traverse the linked list
        
        while current:
            # Fill current position with the value of the current linked list node
            matrix[row][col] = current.val
            current = current.next
            
            # Determine the next position based on the current direction
            next_row = row + directions[curr_direction][0]
            next_col = col + directions[curr_direction][1]
            
            # Check if the next position is out of bounds or already filled
            if not (top_bound <= next_row <= bottom_bound and left_bound <= next_col <= right_bound) or matrix[next_row][next_col] != -1:
                # Change direction clockwise
                curr_direction = (curr_direction + 1) % 4
                next_row = row + directions[curr_direction][0]
                next_col = col + directions[curr_direction][1]
            
            # Move to the next position
            row, col = next_row, next_col

            # Adjust the bounds based on the direction
            if curr_direction == 0:  # moving right
                if col > right_bound:
                    top_bound += 1
            elif curr_direction == 1:  # moving down
                if row > bottom_bound:
                    right_bound -= 1
            elif curr_direction == 2:  # moving left
                if col < left_bound:
                    bottom_bound -= 1
            elif curr_direction == 3:  # moving up
                if row < top_bound:
                    left_bound += 1

        return matrix
m = 3
n = 5
head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
          [[3, 0, 2, 6, 8],
          [5, 0, -1, -1, 1],
          [5, 2, 4, 9, 7]]
