class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Split both sentences into lists of words
        words1 = sentence1.split()
        words2 = sentence2.split()
        
        # Use two pointers to compare the words from the start and end
        i, j = 0, 0
        n1, n2 = len(words1), len(words2)
        
        # Compare the words from the beginning
        while i < n1 and i < n2 and words1[i] == words2[i]:
            i += 1
        
        # Compare the words from the end
        while j < n1 - i and j < n2 - i and words1[-1 - j] == words2[-1 - j]:
            j += 1
        
        # If all words are accounted for (either in the start or end), return True
        return i + j == min(n1, n2)
