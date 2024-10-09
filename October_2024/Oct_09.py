class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0  # To track unmatched '('
        add_count = 0  # To count the moves needed to make valid
        
        for char in s:
            if char == '(':
                balance += 1  # We have an unmatched '('
            elif char == ')':
                if balance > 0:
                    balance -= 1  # A matched pair is found
                else:
                    add_count += 1  # We need an extra '(' for this ')'
        
        # If any unmatched '(' remain, we need closing ')' for them
        return add_count + balance
Input: s = "())"
- Traverse the string:
  - '(' → balance = 1
  - ')' → balance = 0 (valid pair)
  - ')' → no matching '(', increment add_count = 1
- After traversal, balance = 0, add_count = 1.
Output: 1
Input: s = "((("
- Traverse the string:
  - '(' → balance = 1
  - '(' → balance = 2
  - '(' → balance = 3
- After traversal, balance = 3, so we need 3 closing parentheses.
Output: 3
