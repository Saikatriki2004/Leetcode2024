class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Step 1: Sort the unique elements and assign ranks
        sorted_unique = sorted(set(arr))  # Sort unique elements
        
        # Step 2: Create a mapping from element to its rank
        rank_map = {num: rank + 1 for rank, num in enumerate(sorted_unique)}
        
        # Step 3: Replace each element in the original array with its rank
        return [rank_map[num] for num in arr]

# Example usage:
# sol = Solution()
# print(sol.arrayRankTransform([40,10,20,30]))   # Output: [4,1,2,3]
# print(sol.arrayRankTransform([100,100,100]))   # Output: [1,1,1]
# print(sol.arrayRankTransform([37,12,28,9,100,56,80,5,12]))  # Output: [5,3,4,2,8,6,7,1,3]
