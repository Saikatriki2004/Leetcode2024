class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        num = int(n)

        # Handle special cases
        if num <= 10:
            return str(num - 1)
        if n == '11':
            return '9'
        if n == '1' + '0' * (length - 1):
            return str(num - 1)
        if n == '1' + '0' * (length - 1) + '1':
            return str(num + 2)

        # Step 1: Calculate the prefix of the number
        prefix = int(n[:(length + 1) // 2])

        # Step 2: Generate possible palindrome candidates
        candidates = set()
        candidates.add(self.create_palindrome(str(prefix), length % 2 == 0))
        candidates.add(self.create_palindrome(str(prefix - 1), length % 2 == 0))
        candidates.add(self.create_palindrome(str(prefix + 1), length % 2 == 0))
        candidates.add('9' * (length - 1))
        candidates.add('1' + '0' * (length - 1) + '1')

        # Remove the number itself if it's in the set
        candidates.discard(n)

        # Step 3: Find the closest palindrome
        nearest = min(candidates, key=lambda x: (abs(int(x) - num), int(x)))
        return nearest

    def create_palindrome(self, half: str, even: bool) -> str:
        """
        Helper function to create a palindrome by mirroring the half.
        If `even` is True, mirror the entire half.
        If `even` is False, exclude the last digit of half in the mirror.
        """
        if even:
            return half + half[::-1]
        else:
            return half + half[-2::-1]

# Example usage
solution = Solution()
print(solution.nearestPalindromic("1213"))  # Expected output: "1221"
print(solution.nearestPalindromic("123"))   # Expected output: "121"
print(solution.nearestPalindromic("1"))     # Expected output: "0"
