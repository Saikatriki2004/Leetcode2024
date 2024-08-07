#273. Integer to English Words
    class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        # Helper dictionaries
        less_than_20 = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen"
        ]
        tens = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return less_than_20[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return less_than_20[n // 100] + " Hundred " + helper(n % 100)

        res = ""
        i = 0
        
        while num > 0:
            if num % 1000 != 0:
                res = helper(num % 1000) + thousands[i] + " " + res
            num //= 1000
            i += 1

        return res.strip()

# Example usage:
solution = Solution()
print(solution.numberToWords(123))        # "One Hundred Twenty Three"
print(solution.numberToWords(12345))      # "Twelve Thousand Three Hundred Forty Five"
print(solution.numberToWords(1234567))    # "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
print(solution.numberToWords(1234567891)) # "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
