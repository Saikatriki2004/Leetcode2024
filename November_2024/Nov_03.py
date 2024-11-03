class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if lengths are equal and if goal is a substring of s + s
        return len(s) == len(goal) and goal in (s + s)
