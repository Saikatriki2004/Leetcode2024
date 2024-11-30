from collections import defaultdict, deque

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # Build graph and degree maps
        graph = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        
        for a, b in pairs:
            graph[a].append(b)
            out_degree[a] += 1
            in_degree[b] += 1
        
        # Find start node for Eulerian path
        start_node = pairs[0][0]  # Default start
        for node in graph:
            if out_degree[node] - in_degree[node] == 1:
                start_node = node
                break
        
        # Hierholzer's algorithm for Eulerian path
        def eulerian_path(node):
            stack = [node]
            path = []
            while stack:
                while graph[stack[-1]]:
                    next_node = graph[stack[-1]].popleft()
                    stack.append(next_node)
                path.append(stack.pop())
            return path[::-1]
        
        # Get the Eulerian path
        path = eulerian_path(start_node)
        
        # Convert the path into the required pairs format
        result = [[path[i], path[i + 1]] for i in range(len(path) - 1)]
        return result
