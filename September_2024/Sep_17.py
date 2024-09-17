from collections import Counter
from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Split both sentences into words and combine them
        combined_words = s1.split() + s2.split()
        
        # Count the frequency of each word
        word_count = Counter(combined_words)
        
        # Collect words that appear exactly once
        uncommon_words = [word for word in word_count if word_count[word] == 1]
        
        return uncommon_words
