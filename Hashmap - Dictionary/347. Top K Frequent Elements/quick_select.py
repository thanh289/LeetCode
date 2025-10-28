import random
from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        unique = list(freq.keys())

        def quickSelect(arr, target_idx):
            if len(arr) == 1:
                return arr[0]

            pivot = random.choice(arr)
            pivot_freq = freq[pivot]

            lows = [x for x in arr if freq[x] < pivot_freq]
            mids = [x for x in arr if freq[x] == pivot_freq]
            highs = [x for x in arr if freq[x] > pivot_freq]

            if target_idx < len(lows)  :
                return quickSelect(lows, target_idx)
            elif target_idx < len(lows) + len(mids):
                return mids[0]
            else: 
                return quickSelect(highs, target_idx - len(mids) - len(lows))
            
        kth_most_frequent = quickSelect(unique, len(unique)-k)
        return [x for x in unique if freq[x] >= freq[kth_most_frequent]]
     
        
    
sol = Solution()
print(sol.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))

        