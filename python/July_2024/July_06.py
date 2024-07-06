class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        if n == 1:
            return s
        
        start, max_length = 0, 1
        
        def expand_around_center(left: int, right: int) -> None:
            nonlocal start, max_length
            while left >= 0 and right < n and s[left] == s[right]:
                current_length = right - left + 1
                if current_length > max_length:
                    start = left
                    max_length = current_length
                left -= 1
                right += 1
        
        for i in range(n):
            expand_around_center(i, i)
            expand_around_center(i, i + 1)
        
        return s[start:start + max_length]
