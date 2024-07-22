class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Helper function to compute x^n using recursion
        def pow_recursive(x: float, n: int) -> float:
            if n == 0:
                return 1
            elif n < 0:
                x = 1 / x
                n = -n
            
            half = pow_recursive(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
        
        return pow_recursive(x, n)

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(2.00000, 10))   # Output: 1024.00000
    print(sol.myPow(2.10000, 3))    # Output: 9.26100
    print(sol.myPow(2.00000, -2))   # Output: 0.25000
