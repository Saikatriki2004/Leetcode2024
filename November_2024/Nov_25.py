from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Convert the board into a string
        start = ''.join(str(num) for row in board for num in row)
        target = "123450"
        
        # Neighboring indices for each position on a 2x3 board
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        
        # BFS Initialization
        queue = deque([(start, 0)])  # (state, moves)
        visited = {start}
        
        # Perform BFS
        while queue:
            state, moves = queue.popleft()
            
            # Check if we reached the target
            if state == target:
                return moves
            
            # Find the index of '0' and swap with neighbors
            zero_index = state.index('0')
            for neighbor in neighbors[zero_index]:
                new_state = list(state)
                # Swap '0' with the neighbor
                new_state[zero_index], new_state[neighbor] = new_state[neighbor], new_state[zero_index]
                new_state_str = ''.join(new_state)
                
                # If this state has not been visited, add it to the queue
                if new_state_str not in visited:
                    visited.add(new_state_str)
                    queue.append((new_state_str, moves + 1))
        
        # If we exhaust the queue without finding the solution
        return -1
