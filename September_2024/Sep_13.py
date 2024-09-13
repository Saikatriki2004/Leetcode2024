class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Step 1: Create a prefix XOR array
        prefix_xor = [0] * (len(arr) + 1)
        for i in range(1, len(arr) + 1):
            prefix_xor[i] = prefix_xor[i - 1] ^ arr[i - 1]

        # Step 2: Answer each query using the prefix XOR array
        result = []
        for l, r in queries:
            result.append(prefix_xor[r + 1] ^ prefix_xor[l])
        
        return result
