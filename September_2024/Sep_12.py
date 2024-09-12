class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)  # Convert the allowed string to a set for faster lookup
        consistent_count = 0
        
        # Iterate through each word in the list
        for word in words:
            # Check if all characters in the word are in the allowed set
            if all(char in allowed_set for char in word):
                consistent_count += 1
                
        return consistent_count
