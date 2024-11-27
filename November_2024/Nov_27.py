from collections import defaultdict, deque

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Initialize the graph with initial roads
        graph = defaultdict(list)
        for i in range(n - 1):
            graph[i].append(i + 1)
        
        def bfs(start, end):
            # BFS to find the shortest path from start to end
            visited = [False] * n
            queue = deque([(start, 0)])  # (current city, current distance)
            visited[start] = True
            
            while queue:
                current, distance = queue.popleft()
                if current == end:
                    return distance
                
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, distance + 1))
            
            return float('inf')  # If no path exists
        
        result = []
        for u, v in queries:
            graph[u].append(v)  # Add the new edge
            shortest_path = bfs(0, n - 1)
            result.append(shortest_path)
        
        return result
