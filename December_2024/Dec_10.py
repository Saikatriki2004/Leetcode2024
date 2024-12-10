class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        
        # Check for the longest substring of a specific length
        def is_special_and_repeats(length):
            count = {}
            for i in range(n - length + 1):
                # Extract the substring of the given length
                substring = s[i:i + length]
                # Check if it's special (all characters are the same)
                if len(set(substring)) == 1:
                    count[substring] = count.get(substring, 0) + 1
            # Check if any special substring repeats at least 3 times
            return any(c >= 3 for c in count.values())
        
        # Iterate from the longest possible length to the shortest
        for length in range(n, 0, -1):
            if is_special_and_repeats(length):
                return length
        
        return -1

# Example Usage
solution = Solution()
print(solution.maximumLength("aaaa"))  # Output: 2
print(solution.maximumLength("abcdef"))  # Output: -1
print(solution.maximumLength("abcaba"))  # Output: 1
