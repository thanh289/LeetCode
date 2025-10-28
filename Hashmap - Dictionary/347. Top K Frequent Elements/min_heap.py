import heapq # min-heap
from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        
        heap = []
        for x in freq:
            heapq.heappush(heap, (freq[x], x))
            if len(heap) > k:
                heapq.heappop(heap)

        return list(i[1] for i in heap)

        
    
sol = Solution()
print(sol.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))

        