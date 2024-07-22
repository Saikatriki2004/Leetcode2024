class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize stack with base value
        max_length = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
        
        return max_length

# Example usage:
solution = Solution()
print(solution.longestValidParentheses("(()"))        # Output: 2
print(solution.longestValidParentheses(")()())"))     # Output: 4
print(solution.longestValidParentheses(""))           # Output: 0
print(solution.longestValidParentheses("()(()"))      # Output: 2
print(solution.longestValidParentheses("()()"))       # Output: 4
