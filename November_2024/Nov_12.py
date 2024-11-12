from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Sort items by price in ascending order
        items.sort()
        
        # Sort queries with their original indices for result mapping
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        # Initialize variables
        max_beauty = 0
        results = [0] * len(queries)
        idx = 0
        
        # Iterate over sorted queries
        for q_val, q_idx in sorted_queries:
            # Increase max_beauty for all items that are affordable within the query's price
            while idx < len(items) and items[idx][0] <= q_val:
                max_beauty = max(max_beauty, items[idx][1])
                idx += 1
            
            # Assign the max beauty found for this query
            results[q_idx] = max_beauty
            
        return results
