from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = 0
        min_prefix = 0
        result = -float('inf')

        for x in nums:
            prefix_sum += x
            result = max(result, prefix_sum - min_prefix)
            min_prefix = min(min_prefix, prefix_sum)

        return result

# 97 ms, 32.9 MB