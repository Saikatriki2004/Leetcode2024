class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize variables
        result = []
        carry = 0
        
        # Make the strings the same length
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        
        # Iterate from the last digit to the first
        for i in range(max_len - 1, -1, -1):
            # Convert binary characters to integers
            bit_a = int(a[i])
            bit_b = int(b[i])
            
            # Compute the sum of bits and carry
            total = bit_a + bit_b + carry
            result_bit = total % 2
            carry = total // 2
            
            # Append the result bit to the result list
            result.append(str(result_bit))
        
        # If there's a carry left, append it to the result
        if carry:
            result.append(str(carry))
        
        # The result list contains the binary digits in reverse order
        return ''.join(result[::-1])

# Example usage
def test_solution():
    sol = Solution()
    
    print(sol.addBinary("11", "1"))  # Expected: "100"
    print(sol.addBinary("1010", "1011"))  # Expected: "10101"

test_solution()
