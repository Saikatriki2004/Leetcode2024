class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        max_imbalance = 0
        
        # Traverse the string to calculate the maximum imbalance
        for char in s:
            if char == ']':
                balance += 1  # we have one more unmatched closing bracket
            else:
                balance -= 1  # we have one more opening bracket to balance
            
            # Update the maximum imbalance if balance goes positive
            max_imbalance = max(max_imbalance, balance)
        
        # The minimum swaps required to balance is half of the max imbalance
        return (max_imbalance + 1) // 2  # Integer division to get the minimum swaps

# Example usage:
sol = Solution()
print(sol.minSwaps("][]["))  # Output: 1
print(sol.minSwaps("]]][[["))  # Output: 2
print(sol.minSwaps("[]"))  # Output: 0
