from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Lengths of both strings
        len1, len2 = len(s1), len(s2)
        
        # If s1 is longer than s2, there's no way s2 can contain a permutation of s1
        if len1 > len2:
            return False
        
        # Frequency count of s1
        s1_count = Counter(s1)
        
        # Initial window frequency count for the first window of length len1 in s2
        window_count = Counter(s2[:len1])
        
        # Compare the initial window with s1
        if window_count == s1_count:
            return True
        
        # Now slide the window across s2
        for i in range(len1, len2):
            # Include the new character from the right of the window
            window_count[s2[i]] += 1
            
            # Exclude the character from the left of the window
            window_count[s2[i - len1]] -= 1
            
            # Remove the character from the window_count if its count is zero
            if window_count[s2[i - len1]] == 0:
                del window_count[s2[i - len1]]
            
            # Compare the current window with the s1 frequency count
            if window_count == s1_count:
                return True
        
        # No permutation of s1 found in s2
        return False
