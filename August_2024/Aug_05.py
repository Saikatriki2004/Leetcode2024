class Solution:
    def kthDistinct(self, arr, k):
        # Step 1: Count the frequency of each string
        freq = {}
        for string in arr:
            if string in freq:
                freq[string] += 1
            else:
                freq[string] = 1

        # Step 2: Collect the distinct strings
        distinct_strings = []
        for string in arr:
            if freq[string] == 1:
                distinct_strings.append(string)

        # Step 3: Return the kth distinct string if it exists
        if len(distinct_strings) >= k:
            return distinct_strings[k - 1]
        else:
            return ""
# Example usage:
solution = Solution()

arr1 = ["d","b","c","b","c","a"]
k1 = 2
print(solution.kthDistinct(arr1, k1))  # Output: "a"

arr2 = ["aaa","aa","a"]
k2 = 1
print(solution.kthDistinct(arr2, k2))  # Output: "aaa"

arr3 = ["a","b","a"]
k3 = 3
print(solution.kthDistinct(arr3, k3))  # Output: ""          
