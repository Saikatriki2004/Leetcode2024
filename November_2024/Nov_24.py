class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        min_abs_val = float('inf')
        negative_count = 0

        for row in matrix:
            for value in row:
                total_sum += abs(value)
                if value < 0:
                    negative_count += 1
                min_abs_val = min(min_abs_val, abs(value))

        # If the count of negative numbers is odd, subtract twice the smallest absolute value
        if negative_count % 2 == 1:
            total_sum -= 2 * min_abs_val

        return total_sum
