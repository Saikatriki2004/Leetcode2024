from collections import Counter

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # To store the frequency of each signature
        signatures = Counter()

        for row in matrix:
            # Generate the signature normalized to start with 0
            signature = tuple(x ^ row[0] for x in row)
            signatures[signature] += 1

        # Maximum frequency of any signature
        return max(signatures.values())
