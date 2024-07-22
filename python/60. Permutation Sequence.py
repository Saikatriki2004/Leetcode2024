from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Initialize the list of digits
        digits = list(range(1, n + 1))
        
        # Convert k to 0-indexed
        k -= 1
        
        # Initialize the result list
        result = []
        
        # Compute factorials of numbers from 0 to n-1
        fact = [factorial(i) for i in range(n)]
        
        # Determine the permutation
        for i in range(n, 0, -1):
            # Determine the index of the current digit
            idx = k // fact[i - 1]
            # Append the digit at the determined index
            result.append(digits[idx])
            # Remove the used digit
            digits.pop(idx)
            # Update k to reflect the remaining permutations
            k %= fact[i - 1]
        
        return ''.join(map(str, result))

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.getPermutation(3, 3))  # Output: "213"
    print(sol.getPermutation(4, 9))  # Output: "2314"
    print(sol.getPermutation(3, 1))  # Output: "123"
