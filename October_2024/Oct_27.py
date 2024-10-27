class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        # Initialize the DP matrix with the same size as the input matrix
        dp = [[0] * n for _ in range(m)]
        total_squares = 0

        # Traverse the matrix
        for i in range(m):
            for j in range(n):
                # Only consider when the current element is 1
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        # For the first row or column, the value stays the same
                        dp[i][j] = 1
                    else:
                        # Take the minimum of the top, left, and top-left values + 1
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    # Accumulate the count of squares
                    total_squares += dp[i][j]

        return total_squares
