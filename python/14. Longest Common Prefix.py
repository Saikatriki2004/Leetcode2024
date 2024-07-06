class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string in the array as the common prefix
        prefix = strs[0]
        
        # Iterate through each string in the array
        for s in strs[1:]:
            # Check the current prefix with the current string
            while s[:len(prefix)] != prefix:
                # Shorten the prefix by one character until it matches
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
