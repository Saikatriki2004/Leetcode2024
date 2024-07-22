class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        low, high = 0, x
        
        while low <= high:
            mid = (low + high) // 2
            mid_squared = mid * mid
            
            if mid_squared == x:
                return mid
            elif mid_squared < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return high

# Example usage
def test_solution():
    sol = Solution()
    
    print(sol.mySqrt(4))  # Output: 2
    print(sol.mySqrt(8))  # Output: 2
    print(sol.mySqrt(0))  # Output: 0
    print(sol.mySqrt(1))  # Output: 1
    print(sol.mySqrt(16)) # Output: 4
    print(sol.mySqrt(25)) # Output: 5

test_solution()
