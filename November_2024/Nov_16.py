class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
            
        n = len(nums)
        result = []
        window = deque()
        
        for i in range(n):
            # Remove elements outside window
            while window and i - window[0] >= k:
                window.popleft()
                
            # Check consecutive sequence
            if not window or nums[i] - nums[i-1] == 1:
                window.append(i)
            else:
                window.clear()
                window.append(i)
                
            # Add result when window size is k
            if i >= k-1:
                result.append(nums[i] if len(window) == k else -1)
                
        return result
