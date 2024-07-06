class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] will be True if s[0:i] matches p[0:j], else False
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True  # Both s and p are empty
        
        # Fill the table for patterns like a*, a*b*, a*b*c*, etc.
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] if p[j - 2] == s[i - 1] or p[j - 2] == '.' else False)
        
        return dp[len(s)][len(p)]
