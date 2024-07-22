class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        
        if not s or not words:
            return []
        
        word_length = len(words[0])
        num_words = len(words)
        total_length = word_length * num_words
        s_length = len(s)
        
        # If the total length of all words is greater than the length of s, return []
        if total_length > s_length:
            return []
        
        # Count the occurrences of each word in words
        word_count = Counter(words)
        result = []
        
        # Sliding window on each possible starting point
        for i in range(word_length):
            left = i
            right = i
            current_count = Counter()
            while right + word_length <= s_length:
                word = s[right:right + word_length]
                right += word_length
                if word in word_count:
                    current_count[word] += 1
                    # If word count exceeds, move left pointer to balance it
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_length]
                        current_count[left_word] -= 1
                        left += word_length
                    # If the window matches the total length, add to result
                    if right - left == total_length:
                        result.append(left)
                else:
                    # Reset if the word is not in word_count
                    current_count.clear()
                    left = right
        return result
