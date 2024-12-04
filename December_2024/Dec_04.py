class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0
        n, m = len(str1), len(str2)
        
        while i < n and j < m:
            # Check if characters match directly or after cyclic increment
            if str1[i] == str2[j] or chr((ord(str1[i]) - ord('a') + 1) % 26 + ord('a')) == str2[j]:
                j += 1  # Match found, move pointer for str2
            i += 1  # Always move pointer for str1
        
        # If all characters of str2 are matched, return True
        return j == m
