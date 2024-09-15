class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Dictionary to store the first occurrence of each bitmask
        first_occurrence = {0: -1}
        # Initialize variables
        bitmask = 0
        max_length = 0
        # Vowels set
        vowels = 'aeiou'
        
        for i, char in enumerate(s):
            if char in vowels:
                # Update bitmask for vowels
                bitmask ^= 1 << vowels.index(char)
            
            # Check if this bitmask has been seen before
            if bitmask in first_occurrence:
                # Calculate the length of the substring
                length = i - first_occurrence[bitmask]
                max_length = max(max_length, length)
            else:
                # Store the first occurrence of this bitmask
                first_occurrence[bitmask] = i
        
        return max_length
