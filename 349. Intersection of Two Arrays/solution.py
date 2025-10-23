from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        result = []
        for x in set1:
            if x in set2:
                result.append(x)
        return result
    #   return list(set1 & set2)