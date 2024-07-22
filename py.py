class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

# Example usage
sol = Solution()c
print(sol.strStr("sadbutsad", "sad"))  # Output: 0
print(sol.strStr("leetcode", "leeto"))  # Output: -1
