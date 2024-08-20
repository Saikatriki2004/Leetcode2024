class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # Suffix sum array to calculate the remaining stones in O(1)
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        
        # Memoization table
        memo = {}
        
        def dp(i, M):
            if i >= n: 
                return 0
            if (i, M) in memo:
                return memo[(i, M)]
            
            max_stones = 0
            for x in range(1, 2 * M + 1):
                if i + x > n:
                    break
                max_stones = max(max_stones, suffix_sum[i] - dp(i + x, max(M, x)))
            
            memo[(i, M)] = max_stones
            return max_stones
        
        return dp(0, 1)
#Example:      
piles = [2, 7, 9, 4, 4]
sol = Solution()
print(sol.stoneGameII(piles))  # Output: 10
