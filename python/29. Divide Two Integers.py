class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for the 32-bit signed integer range
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        # Special cases
        if dividend == 0:
            return 0
        if divisor == 1:
            return min(MAX_INT, max(MIN_INT, dividend))
        if divisor == -1:
            return min(MAX_INT, max(MIN_INT, -dividend))
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive values for simplicity
        dividend, divisor = abs(dividend), abs(divisor)
        
        # Perform the division using bit manipulation
        quotient = 0
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            dividend -= temp_divisor
            quotient += multiple
        
        # Apply the sign to the result
        if negative:
            quotient = -quotient
        
        # Clamp the result to the 32-bit signed integer range
        return min(MAX_INT, max(MIN_INT, quotient))

# Example usage
sol = Solution()
print(sol.divide(10, 3))   # Output: 3
print(sol.divide(7, -3))   # Output: -2
print(sol.divide(0, 1))    # Output: 0
print(sol.divide(1, 1))    # Output: 1
