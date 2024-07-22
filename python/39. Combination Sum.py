class Solution:
    def combinationSum(self, candidates, target):
        def backtrack(start, target, path):
            # Base case: if the target is met, add the path to results
            if target == 0:
                result.append(path)
                return
            # Try each candidate
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                if candidate > target:
                    continue  # No need to continue if candidate exceeds the target
                # Recurse with the updated target and path
                backtrack(i, target - candidate, path + [candidate])
        
        result = []
        candidates.sort()  # Optional, for better pruning
        backtrack(0, target, [])
        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([2, 3, 6, 7], 7))  # Output: [[2,2,3],[7]]
    print(sol.combinationSum([2, 3, 5], 8))     # Output: [[2,2,2,2],[2,3,3],[3,5]]
    print(sol.combinationSum([2], 1))            # Output: []
