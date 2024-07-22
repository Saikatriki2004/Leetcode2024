class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_line = []
        current_length = 0
        
        # Helper function to justify a line
        def justify_line(line: List[str], length: int, is_last: bool) -> str:
            if len(line) == 1 or is_last:
                # For the last line or single word line, left-justify
                return ' '.join(line).ljust(maxWidth)
            total_spaces = maxWidth - length
            spaces_needed = len(line) - 1
            space_between_words = total_spaces // spaces_needed
            extra_spaces = total_spaces % spaces_needed
            
            line_str = ''
            for i in range(spaces_needed):
                line_str += line[i]
                line_str += ' ' * (space_between_words + (1 if i < extra_spaces else 0))
            line_str += line[-1]  # Append the last word
            return line_str
        
        # Process each word
        for word in words:
            if current_length + len(word) + len(current_line) > maxWidth:
                result.append(justify_line(current_line, current_length, False))
                current_line = []
                current_length = 0
            
            current_line.append(word)
            current_length += len(word)
        
        # Process the last line
        if current_line:
            result.append(justify_line(current_line, current_length, True))
        
        return result

# Example usage
def test_solution():
    sol = Solution()
    
    print(sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
    print(sol.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))
    print(sol.fullJustify(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20))

test_solution()
