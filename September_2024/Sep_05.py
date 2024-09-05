from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)  # Number of existing rolls
        total_sum_needed = mean * (m + n)  # Total sum required for m + n rolls
        current_sum = sum(rolls)  # Sum of the given rolls
        missing_sum = total_sum_needed - current_sum  # Sum that the missing rolls must add up to
        
        # Check if it's possible to get the missing sum with n rolls
        if missing_sum < n or missing_sum > 6 * n:
            return []  # Impossible to find such rolls
        
        # Initialize the missing rolls as an array of 1's
        missing_rolls = [1] * n
        remaining_sum = missing_sum - n  # Subtract n because we already set each roll to 1
        
        # Distribute the remaining sum across the missing rolls
        i = 0
        while remaining_sum > 0:
            add = min(5, remaining_sum)  # We can add at most 5 to each roll (1 + 5 = 6)
            missing_rolls[i] += add
            remaining_sum -= add
            i += 1
        
        return missing_rolls
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1:
    rolls = [3, 2, 4, 3]
    mean = 4
    n = 2
    result = sol.missingRolls(rolls, mean, n)
    print(result)  # Output might be [6, 6] or [5, 6] depending on distribution
