from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for word in strs:
            # Create a key by sorting the characters in the word
            key = tuple(sorted(word))
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
        
        # Collect all grouped anagrams
        return list(anagrams.values())

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
