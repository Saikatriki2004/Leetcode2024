class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Start from the end of the list
        for i in range(len(digits) - 1, -1, -1):
            # Increment the current digit
            digits[i] += 1
            # Check if there is a carry
            if digits[i] < 10:
                return digits
            # If there is a carry, set current digit to 0 and continue with the carry
            digits[i] = 0
        
        # If we have finished the loop, all digits were 9, so we need to add a new digit
        return [1] + digits
