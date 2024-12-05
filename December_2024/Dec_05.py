class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Extract indices and characters of 'L' and 'R' from both strings
        start_positions = [(c, i) for i, c in enumerate(start) if c in 'LR']
        target_positions = [(c, i) for i, c in enumerate(target) if c in 'LR']
        
        # Check if the characters and their counts match
        if len(start_positions) != len(target_positions):
            return False
        
        for (start_char, start_idx), (target_char, target_idx) in zip(start_positions, target_positions):
            # Characters must match
            if start_char != target_char:
                return False
            # Check movement constraints
            if start_char == 'L' and start_idx < target_idx:
                return False
            if start_char == 'R' and start_idx > target_idx:
                return False
        
        return True
