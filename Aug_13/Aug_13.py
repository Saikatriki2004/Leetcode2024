class Solution:
    def combinationSum2(self, candidates, target):
        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break  # No need to continue if the candidate exceeds the target
                # Recursively try the next numbers
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])
        
        result = []
        candidates.sort()  # Sort to handle duplicates and pruning
        backtrack(0, target, [])
        return result
     
