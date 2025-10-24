from cmath import inf
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf
        f = 0
        for x in nums:
            if f > 0:
                f = f + x
            else:
                f = x
            # don't use max, it'll take longer
            if f > ans:
                ans = f
        return ans
    
# 15 ms, 32.9 MB
