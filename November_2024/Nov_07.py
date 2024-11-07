class Solution:
    def largestCombination(self, candidates):
        max_bits = 24  # Since candidates[i] <= 10^7, we only need 24 bits
        bit_counts = [0] * max_bits
        
        # Count the number of candidates that have each bit set
        for num in candidates:
            for bit in range(max_bits):
                if num & (1 << bit):
                    bit_counts[bit] += 1
        
        # The answer is the maximum count found in any bit position
        return max(bit_counts)
