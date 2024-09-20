class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Create the augmented string: s + '#' + reverse(s)
        rev_s = s[::-1]
        new_s = s + '#' + rev_s
        
        # Compute the KMP table (partial match table)
        n = len(new_s)
        lps = [0] * n  # lps stands for longest proper prefix which is also suffix
        
        # Build the LPS array for new_s
        for i in range(1, n):
            j = lps[i - 1]  # Start by looking at the previous longest prefix-suffix length
            while j > 0 and new_s[i] != new_s[j]:
                j = lps[j - 1]  # Fallback to the next best candidate
            if new_s[i] == new_s[j]:
                j += 1
            lps[i] = j
        
        # The length of the longest palindromic prefix is given by lps[-1]
        longest_palindrome_prefix_len = lps[-1]
        
        # The suffix to be added is the reverse of the remaining part of the string
        suffix_to_add = s[longest_palindrome_prefix_len:][::-1]
        
        return suffix_to_add + s
