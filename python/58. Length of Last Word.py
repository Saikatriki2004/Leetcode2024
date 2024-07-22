class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Step 1: Strip trailing spaces
        s = s.rstrip()
        
        # Step 2: Find the last word by splitting
        # Split the string by spaces
        words = s.split()
        
        # The last word will be the last element of the split list
        last_word = words[-1]
        
        # Return the length of the last word
        return len(last_word)

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLastWord("Hello World"))  # Output: 5
    print(sol.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
    print(sol.lengthOfLastWord("luffy is still joyboy"))  # Output: 6
