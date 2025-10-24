from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check = {}
        for x in nums:
            if x in check:
                return x
            check[x] = 1
            
# 24 ms, 39.4 MB, can use set for better time