class Solution:
    def countSeniors(self, details):
        count = 0
        for detail in details:
            # Extract the age which is at the 11th and 12th positions in the string
            age = int(detail[11:13])
            if age > 60:
                count += 1
        return count

# Example usage:
solution = Solution()
details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
print(solution.countSeniors(details))  # Output: 2

details = ["1313579440F2036", "2921522980M5644"]
print(solution.countSeniors(details))  # Output: 0
