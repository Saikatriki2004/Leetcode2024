class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # Convert banned list to a set for faster lookups
        banned_set = set(banned)
        
        current_sum = 0
        count = 0
        
        # Iterate over integers from 1 to n
        for i in range(1, n + 1):
            # Skip banned numbers
            if i in banned_set:
                continue
            
            # Check if adding the current number exceeds maxSum
            if current_sum + i > maxSum:
                break
            
            # Add the current number to the sum and increase the count
            current_sum += i
            count += 1
        
        return count
