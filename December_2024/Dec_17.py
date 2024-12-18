from collections import Counter
import heapq

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        max_heap = [(-ord(ch), ch, count) for ch, count in freq.items()]
        heapq.heapify(max_heap)
        
        result = []
        
        while max_heap:
            _, ch, count = heapq.heappop(max_heap)
            allowed = min(count, repeatLimit)
            result.append(ch * allowed)
            
            count -= allowed
            if count > 0:
                if not max_heap:
                    break
                _, next_ch, next_count = heapq.heappop(max_heap)
                result.append(next_ch)
                next_count -= 1
                
                if next_count > 0:
                    heapq.heappush(max_heap, (-ord(next_ch), next_ch, next_count))
                heapq.heappush(max_heap, (-ord(ch), ch, count))
        
        return ''.join(result)
