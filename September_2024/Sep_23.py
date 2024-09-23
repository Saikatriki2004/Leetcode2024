class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Convert the dictionary list into a set for faster lookup
        word_set = set(dictionary)
        
        # Length of the string
        n = len(s)
        
        # DP array to store the minimum number of extra characters at each index
        dp = [0] * (n + 1)
        
        # Initialize the DP array
        for i in range(1, n + 1):
            # Assume the worst case: the substring s[0:i] has no valid dictionary word
            dp[i] = dp[i - 1] + 1
            
            # Check for each possible j if s[j:i] is in the dictionary
            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])

        # The answer is the minimum extra characters for the entire string
        return dp[n]
