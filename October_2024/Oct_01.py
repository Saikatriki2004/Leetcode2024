class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # Array to store the frequency of remainders
        remainder_count = [0] * k
        
        # Calculate the remainder frequencies
        for num in arr:
            remainder = num % k
            if remainder < 0:
                remainder += k  # Ensure remainder is positive
            remainder_count[remainder] += 1
        
        # Check pairs for remainder 0
        if remainder_count[0] % 2 != 0:
            return False
        
        # Check pairs for remainders 1 to k-1
        for i in range(1, k):
            if remainder_count[i] != remainder_count[k - i]:
                return False
        
        # If all conditions are satisfied, return True
        return True
