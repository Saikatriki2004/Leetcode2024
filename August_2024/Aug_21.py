class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n-1, -1, -1):  # Traverse from the end to the beginning
            dp[i][i] = 1  # Base case: Single character
            for j in range(i + 1, n):
                dp[i][j] = dp[i][j-1] + 1  # Start by considering a new print
                for k in range(i, j):
                    if s[k] == s[j]:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j-1])
        
        return dp[0][n-1]

# Example usage:
solution = Solution()
print(solution.strangePrinter("aaabbb"))  # Output: 2
print(solution.strangePrinter("aba"))     # Output: 2
