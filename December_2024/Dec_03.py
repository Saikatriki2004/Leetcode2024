class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        space_idx = 0
        n = len(spaces)
        
        for i in range(len(s)):
            # If current index matches a space index, add a space
            if space_idx < n and i == spaces[space_idx]:
                result.append(' ')
                space_idx += 1
            result.append(s[i])
        
        return ''.join(result)
