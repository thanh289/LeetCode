from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] * nums[i-1])

        suffix = [1]
        for i in range(len(nums)-2, -1, -1):
            suffix.append(suffix[-1] * nums[i+1])

        suffix.reverse()
        result = [prefix[i] * suffix[i] for i in range(len(nums))]
        return result
    
# 32 ms, 27 MB