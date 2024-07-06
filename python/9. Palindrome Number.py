class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Numbers ending in 0 (except 0 itself) are not palindromes
        if x % 10 == 0 and x != 0:
            return False
        
        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
        
        # When the length is an odd number, we can get rid of the middle digit by reverted_number // 10
        return x == reverted_number or x == reverted_number // 10
