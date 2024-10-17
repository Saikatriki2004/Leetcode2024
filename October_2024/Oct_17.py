class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of digits for easy manipulation
        digits = list(str(num))
        
        # Store the last occurrence index of each digit (0-9)
        last_occurrence = {int(d): i for i, d in enumerate(digits)}
        
        # Traverse the digits from left to right
        for i, d in enumerate(digits):
            # Check if there exists a larger digit in the remaining part of the number
            for larger_digit in range(9, int(d), -1):
                if last_occurrence.get(larger_digit, -1) > i:
                    # Swap the current digit with the largest possible digit
                    j = last_occurrence[larger_digit]
                    digits[i], digits[j] = digits[j], digits[i]
                    # Return the new number after the swap
                    return int(''.join(digits))
        
        # If no swap is made, return the original number
        return num

# Example usage:
solution = Solution()
print(solution.maximumSwap(2736))  # Output: 7236
print(solution.maximumSwap(9973))  # Output: 9973
