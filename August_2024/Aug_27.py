import heapq
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Create a graph from edges and succProb
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        # Max heap for Dijkstra's algorithm, using -probability for max-heap behavior
        heap = [(-1.0, start_node)]
        max_prob = [0.0] * n
        max_prob[start_node] = 1.0

        while heap:
            prob, node = heapq.heappop(heap)
            prob = -prob  # Convert back to positive probability

            if node == end_node:
                return prob

            for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(heap, (-new_prob, neighbor))

        return 0.0
# Example usage
n = 5
edges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 4]]
succProb = [0.5, 0.4, 0.3, 0.8, 0.7]
start_node = 0
end_node = 4

solution = Solution()
result = solution.maxProbability(n, edges, succProb, start_node, end_node)
print(f"Maximum Probability: {result}")
