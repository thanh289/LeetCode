import math
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zero = nums.count(0)

        if count_zero > 1:
            return [0] * len(nums)
        
        if count_zero == 1:
            total_product = math.prod(x for x in nums if x != 0)
            return [total_product if x == 0 else 0 for x in nums]
        
        if count_zero == 0:
            total_product = math.prod(nums)
            return [total_product//x for x in nums]
        
# 7 ms, 23.3 MB