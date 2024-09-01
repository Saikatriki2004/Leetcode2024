from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Check if it's possible to form an m x n array
        if len(original) != m * n:
            return []
        
        # Create the 2D array
        result = []
        for i in range(m):
            row = original[i * n:(i + 1) * n]  # Slice the original array to form each row
            result.append(row)
        
        return result

# Example usage:
solution = Solution()

original = [1, 2, 3, 4, 5, 6]
m = 2
n = 3
print(solution.construct2DArray(original, m, n))  # Expected Output: [[1, 2, 3], [4, 5, 6]]

original = [1, 2, 3]
m = 1
n = 3
print(solution.construct2DArray(original, m, n))  # Expected Output: [[1, 2, 3]]

original = [1, 2]
m = 1
n = 3
print(solution.construct2DArray(original, m, n))  # Expected Output: []
