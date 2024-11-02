class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        
        # Check each word's last character with the next word's first character
        for i in range(len(words)):
            if words[i][-1] != words[(i + 1) % len(words)][0]:
                return False
        
        return True
