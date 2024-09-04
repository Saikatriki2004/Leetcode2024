class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Step 1: Convert each character in the string to its corresponding position
        numeric_string = ''.join(str(ord(char) - ord('a') + 1) for char in s)
        
        # Step 2: Calculate the sum of the digits
        def digit_sum(num_str):
            return sum(int(digit) for digit in num_str)
        
        # Apply the digit sum process k times
        for _ in range(k):
            numeric_string = str(digit_sum(numeric_string))
        
        return int(numeric_string)
