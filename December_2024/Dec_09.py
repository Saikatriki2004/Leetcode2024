from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        # Step 1: Precompute parity and prefix sums
        parity = [0] * n
        prefixParity = [0] * n
        
        # Compute parity array
        for i in range(1, n):
            if (nums[i] % 2) != (nums[i-1] % 2):  # Different parity
                parity[i] = 1

        # Compute prefix sum of parity array
        for i in range(1, n):
            prefixParity[i] = prefixParity[i-1] + parity[i]

        # Step 2: Process queries
        result = []
        for l, r in queries:
            if r == l:  # Single element is always special
                result.append(True)
            else:
                # Check if all adjacent elements in the range [l, r] have different parity
                totalParity = prefixParity[r] - prefixParity[l]
                result.append(totalParity == (r - l))
        
        return result

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [4, 3, 1, 6]
    queries = [[0, 2], [2, 3]]
    print(solution.isArraySpecial(nums, queries))  # Output: [False, True]
