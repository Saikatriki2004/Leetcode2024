class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # Create a DP table with dimensions (m+1) x (n+1)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty pattern matches empty string
        dp[0][0] = True
        
        # Base case: patterns with '*' can match empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' can match empty sequence or non-empty sequence
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    # '?' matches any single character or exact character match
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[m][n]

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.isMatch("aa", "a"))    # Output: False
    print(sol.isMatch("aa", "*"))    # Output: True
    print(sol.isMatch("cb", "?a"))   # Output: False
