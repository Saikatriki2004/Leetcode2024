from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Splitting the input expression into fractions
        fractions = []
        i = 0
        while i < len(expression):
            if expression[i] in '+-':
                j = i + 1
            else:
                j = i
            while j < len(expression) and expression[j] not in '+-':
                j += 1
            fractions.append(Fraction(expression[i:j]))
            i = j
        
        # Summing up all the fractions
        result = sum(fractions)
        
        # Converting the result to a string in the form "numerator/denominator"
        return f'{result.numerator}/{result.denominator}'

# Example Usage
solution = Solution()
expression = "-1/2+1/2+1/3"
print(solution.fractionAddition(expression))  # Output: "1/3"
