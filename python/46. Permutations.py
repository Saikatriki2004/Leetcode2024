class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(first=0):
            # Base case: if all integers are used up
            if first == n:
                result.append(nums[:])
            for i in range(first, n):
                # Swap the current element with the first element
                nums[first], nums[i] = nums[i], nums[first]
                # Recurse on the remaining elements
                backtrack(first + 1)
                # Backtrack (swap back)
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        result = []
        backtrack()
        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1, 2, 3]))  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    print(sol.permute([0, 1]))     # Output: [[0, 1], [1, 0]]
    print(sol.permute([1]))        # Output: [[1]]
