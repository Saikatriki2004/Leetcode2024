class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        
        # Sort intervals based on the starting values
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        for interval in intervals:
            # If merged is empty or there is no overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # There is an overlap, merge the intervals
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))  # Output: [[1,6],[8,10],[15,18]]
    print(sol.merge([[1,4],[4,5]]))  # Output: [[1,5]]
