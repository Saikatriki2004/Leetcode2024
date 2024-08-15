from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            elif bill == 20:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        
        return True
sol = Solution()

# Test case 1: [5, 5, 10, 10, 20]
print(sol.lemonadeChange([5, 5, 10, 10, 20]))  # Expected output: False

# Test case 2: [5, 5, 5, 10, 20]
print(sol.lemonadeChange([5, 5, 5, 10, 20]))  # Expected output: True
