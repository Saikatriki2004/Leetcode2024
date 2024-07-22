class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge case: if any number is "0", return "0"
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        # Initialize result array with zeroes
        result = [0] * (m + n)
        
        # Reverse iterate over both strings
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # Multiply the digits
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                # Position in the result array
                p1, p2 = i + j, i + j + 1
                # Add multiplication result to the corresponding position
                sum_ = mul + result[p2]
                
                # Update the result array
                result[p2] = sum_ % 10
                result[p1] += sum_ // 10
        
        # Convert result array to string, skipping leading zeroes
        result_str = ''.join(map(str, result))
        return result_str.lstrip('0')

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.multiply("2", "3"))    # Output: "6"
    print(sol.multiply("123", "456")) # Output: "56088"
