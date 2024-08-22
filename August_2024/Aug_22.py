class Solution:
    def findComplement(self, num: int) -> int:
        # Step 1: Find the bit length of the number
        bit_length = num.bit_length()
        
        # Step 2: Create a mask with all bits set to 1 of the same length as num
        mask = (1 << bit_length) - 1
        
        # Step 3: XOR the number with the mask to get the complement
        return num ^ mask
# Example 1
num = 5
solution = Solution()
print(solution.findComplement(num))  # Output: 2

# Example 2
num = 1
print(solution.findComplement(num))  # Output: 0
