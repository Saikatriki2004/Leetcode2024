class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR start and goal to find bits that differ
        xor_result = start ^ goal
        
        # Count the number of 1s in the binary representation of xor_result
        return bin(xor_result).count('1')
