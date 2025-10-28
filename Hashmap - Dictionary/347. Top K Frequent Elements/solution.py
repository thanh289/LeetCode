from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        dic = dict(sorted(dic.items(), key=lambda item:item[1], reverse=True))
        result = []

        for x in dic:
            if len(result) < k:
                result.append(x)
            else:
                break
        return result

        
    
sol = Solution()
print(sol.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))

        