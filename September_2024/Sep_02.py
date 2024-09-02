from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        total = sum(chalk)
        k %= total  # reduce k to its equivalent value within one cycle
        
        for i in range(n):
            if k < chalk[i]:
                return i
            k -= chalk[i]
        
        # if we reach this point, it means k is a multiple of total
        # so we return 0, because the first student will replace the chalk
        return 0
