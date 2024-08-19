class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        # Initialize step count
        steps = 0
        factor = 2
        
        # Factorize n by dividing by the smallest possible factors
        while n > 1:
            while n % factor == 0:
                steps += factor
                n //= factor
            factor += 1
        
        return steps
sol = Solution()
print(sol.minSteps(6))  # Output should be 5
