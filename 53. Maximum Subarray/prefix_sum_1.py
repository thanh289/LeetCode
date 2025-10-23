from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = [0]
        for i in range(len(nums)):
            sums.append(sums[i] + nums[i])
        
        result = nums[0]
        minimum = sums[0]

        for i in range(1, len(sums)):
            if sums[i] < minimum:
                minimum = sums[i]
            else:
                result = max(result, sums[i] - minimum)
        return max(result, max(nums))
    
    # 74 ms, 33.2 MB
    # this one is faster than ver 2 but the logic is not that good since this one was made by knowing the wrong testcase
    # still better to use the version 2
    

