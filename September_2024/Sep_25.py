class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0  # To store how many times the prefix appears

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # Step 1: Build the Trie and count prefixes
        root = TrieNode()
        
        # Insert a word into the Trie
        def insert(word):
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                node.count += 1
        
        # Insert all words into the Trie
        for word in words:
            insert(word)
        
        # Step 2: Calculate the prefix score for each word
        def calculate_score(word):
            node = root
            score = 0
            for char in word:
                node = node.children[char]
                score += node.count
            return score
        
        # Step 3: Create the result array
        result = []
        for word in words:
            result.append(calculate_score(word))
        
        return result
