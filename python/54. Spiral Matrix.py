class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:
            return []
        
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # Traverse from left to right along the top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            
            # Traverse from top to bottom along the right column
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            
            if top <= bottom:
                # Traverse from right to left along the bottom row
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            
            if left <= right:
                # Traverse from bottom to top along the left column
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        
        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))  # Output: [1,2,3,6,9,8,7,4,5]
    print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))  # Output: [1,2,3,4,8,12,11,10,9,5,6,7]
