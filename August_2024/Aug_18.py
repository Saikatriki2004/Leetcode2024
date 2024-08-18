class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Initialize the ugly number list
        ugly_numbers = [0] * n
        ugly_numbers[0] = 1
        
        # Initialize indices for 2, 3, and 5
        i2 = i3 = i5 = 0
        
        # Initialize the first multiples of 2, 3, and 5
        next_2 = 2
        next_3 = 3
        next_5 = 5
        
        # Generate n ugly numbers
        for i in range(1, n):
            # Select the smallest next number
            next_ugly = min(next_2, next_3, next_5)
            ugly_numbers[i] = next_ugly
            
            # Increment the index that contributed to the smallest value
            if next_ugly == next_2:
                i2 += 1
                next_2 = ugly_numbers[i2] * 2
            if next_ugly == next_3:
                i3 += 1
                next_3 = ugly_numbers[i3] * 3
            if next_ugly == next_5:
                i5 += 1
                next_5 = ugly_numbers[i5] * 5
        
        return ugly_numbers[-1]
sol = Solution()
print(sol.nthUglyNumber(10))  # Output: 12
