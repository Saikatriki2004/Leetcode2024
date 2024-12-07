class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def canDivide(mid):
            operations = 0
            for balls in nums:
                # Calculate how many operations are needed to make all bags ≤ mid
                if balls > mid:
                    operations += (balls - 1) // mid
            return operations <= maxOperations

        # Binary search range
        left, right = 1, max(nums)
        result = right

        while left <= right:
            mid = (left + right) // 2
            if canDivide(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
