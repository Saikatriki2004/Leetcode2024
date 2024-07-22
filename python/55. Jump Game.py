class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest = 0
        n = len(nums)
        
        for i in range(n):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= n - 1:
                return True
        
        return False

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.canJump([2, 3, 1, 1, 4]))  # Output: True
    print(sol.canJump([3, 2, 1, 0, 4]))  # Output: False
