from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Done 2 loops the first time, now try with hashmap
        seen = {}
        for i, num in enumerate(nums):
            check = target - num
            if check in seen:
                return [seen[check], i]
            seen[num] = i


# 0 ms, 19.1 MB