import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # Regular expression to match a valid number
        pattern = re.compile(r'''
            ^[+-]?                           # Optional sign
            (                               
                (\d+(\.\d*)?)               # Integer or Decimal without exponent
                |                           
                (\.\d+)                      # Decimal without integer part
            )
            ([eE][+-]?\d+)?                  # Optional exponent part
            $                                # End of string
        ''', re.VERBOSE)
        
        return pattern.match(s) is not None
# Example test cases
def test_solution():
    sol = Solution()
    
    print(sol.isNumber("0"))            # Expected: True
    print(sol.isNumber("e"))            # Expected: False
    print(sol.isNumber("."))            # Expected: False
    print(sol.isNumber("2e10"))         # Expected: True
    print(sol.isNumber("-123.456e789")) # Expected: True
    print(sol.isNumber("95a54e53"))     # Expected: False
    print(sol.isNumber("   1.1e-1 "))   # Expected: True (with leading/trailing spaces)

test_solution()
