from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Direction vectors: North, East, South, West
        direction_vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Start facing North
        current_direction = 0
        
        # Convert obstacles to a set of tuples for quick lookup
        obstacle_set = set(map(tuple, obstacles))
        
        # Initial position
        x, y = 0, 0
        max_distance_squared = 0
        
        for command in commands:
            if command == -2:  # Turn left
                current_direction = (current_direction + 3) % 4
            elif command == -1:  # Turn right
                current_direction = (current_direction + 1) % 4
            else:  # Move forward command units
                dx, dy = direction_vectors[current_direction]
                for _ in range(command):
                    if (x + dx, y + dy) not in obstacle_set:
                        x += dx
                        y += dy
                        # Update the max distance squared from the origin
                        max_distance_squared = max(max_distance_squared, x**2 + y**2)
                    else:
                        break
        
        return max_distance_squared

# Example usage:
sol = Solution()
commands = [4, -1, 3]
obstacles = []
print(sol.robotSim(commands, obstacles))  # Output should be 25

commands = [4, -1, 4, -2, 4]
obstacles = [[2, 4]]
print(sol.robotSim(commands, obstacles))  # Output should be 65
