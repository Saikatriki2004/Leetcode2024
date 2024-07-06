class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # Define the mapping from digits to letters
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        # List to store the final combinations
        combinations = []
        
        # Backtracking function
        def backtrack(index, current):
            # If the current combination is of the required length
            if len(current) == len(digits):
                combinations.append("".join(current))
                return
            
            # Get the letters corresponding to the current digit
            letters = digit_to_letters[digits[index]]
            
            # Iterate through each letter
            for letter in letters:
                # Add the letter to the current combination
                current.append(letter)
                # Recursively call backtrack for the next digit
                backtrack(index + 1, current)
                # Backtrack: remove the last added letter
                current.pop()
        
        # Start backtracking from the first digit
        backtrack(0, [])
        
        return combinations
