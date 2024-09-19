class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Base case: if the expression is just a number
        if expression.isdigit():
            return [int(expression)]

        results = []
        
        # Split the expression at every operator
        for i, char in enumerate(expression):
            if char in "+-*":
                # Recursively solve for left and right parts
                left_results = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i+1:])
                
                # Combine results using the operator
                for left in left_results:
                    for right in right_results:
                        if char == '+':
                            results.append(left + right)
                        elif char == '-':
                            results.append(left - right)
                        elif char == '*':
                            results.append(left * right)
        
        return results
expression = "2-1-1"
solution = Solution()
output = solution.diffWaysToCompute(expression)
print(output)

expression = "2*3-4*5"
solution = Solution()
output = solution.diffWaysToCompute(expression)
print(output)
