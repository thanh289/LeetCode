from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums = list(set(nums))
        # A lot of other solutions just use set, no need for list
        nums.sort()
        # print(nums)
        result, count = 1, 1
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                count += 1
            else:
                result = max(result, count)
                count = 1
        result = max(result, count)
        return result
    
sol = Solution()
print(sol.longestConsecutive([100,4,200,1,3,2]))
        