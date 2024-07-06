class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1  # Maximum 32-bit signed integer value
        INT_MIN = -2**31     # Minimum 32-bit signed integer value
        
        result = 0
        is_negative = x < 0
        x = abs(x)
        
        while x != 0:
            pop = x % 10  # Get the last digit
            x //= 10      # Remove the last digit from x
            
            # Check for overflow before multiplying and adding
            if result > (INT_MAX - pop) / 10:
                return 0
            
            result = result * 10 + pop
        
        if is_negative:
            result = -result
        
        return result if INT_MIN <= result <= INT_MAX else 0
