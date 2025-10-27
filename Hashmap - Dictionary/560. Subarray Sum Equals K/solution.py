from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Dict used to save the number of prefix sum
        dict = {0:1}

        prefix = 0
        result = 0
        for i in range (len(nums)):
            prefix += nums[i]
            if (prefix-k) in dict:
                result += dict[prefix-k]
            dict[prefix] = dict.get(prefix, 0) + 1
        return result
        
sol = Solution()
print(sol.subarraySum([2], 2))
