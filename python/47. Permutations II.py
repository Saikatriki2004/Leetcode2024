class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                    continue
                
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used[i] = False

        nums.sort()  # Sort to handle duplicates
        result = []
        used = [False] * len(nums)
        backtrack([], used)
        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.permuteUnique([1, 1, 2]))  # Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    print(sol.permuteUnique([1, 2, 3]))  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
