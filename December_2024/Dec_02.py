class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # Split the sentence into words
        words = sentence.split()
        
        # Iterate over the words with their 1-based index
        for index, word in enumerate(words, start=1):
            # Check if searchWord is a prefix of the current word
            if word.startswith(searchWord):
                return index
        
        # If no word satisfies the condition, return -1
        return -1
