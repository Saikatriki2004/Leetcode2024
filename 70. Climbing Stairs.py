class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize base cases
        dp1, dp2 = 1, 2
        
        for i in range(3, n + 1):
            # Calculate the number of ways to reach the i-th step
            dp = dp1 + dp2
            dp1, dp2 = dp2, dp
        
        return dp2

# Example usage
def test_solution():
    sol = Solution()
    
    print(sol.climbStairs(2))  # Output: 2
    print(sol.climbStairs(3))  # Output: 3
    print(sol.climbStairs(4))  # Output: 5
    print(sol.climbStairs(5))  # Output: 8

test_solution()
