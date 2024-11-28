from collections import deque

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dist = [[float('inf')] * n for _ in range(m)]  # To track the minimum obstacles removed
        dist[0][0] = 0
        
        deque_queue = deque([(0, 0, 0)])  # (cost, x, y)
        
        while deque_queue:
            cost, x, y = deque_queue.popleft()
            
            if (x, y) == (m - 1, n - 1):
                return cost  # Reached the destination
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = cost + grid[nx][ny]  # Add 1 if obstacle, else add 0
                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        if grid[nx][ny] == 0:
                            deque_queue.appendleft((new_cost, nx, ny))  # Empty cell, prioritize
                        else:
                            deque_queue.append((new_cost, nx, ny))  # Obstacle cell
            
        return -1  # This shouldn't happen given the constraints
