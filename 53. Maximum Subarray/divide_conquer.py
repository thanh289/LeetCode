from cmath import inf
from typing import List


from cmath import inf
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(left: int, right: int) -> int:
            if (left == right):
                return nums[left]
            
            mid = (left + right) // 2

            left_max = helper(left, mid)
            right_max = helper(mid+1, right)

            left_sum = -inf
            temp = 0
            for i in range(mid, left-1, -1):
                temp += nums[i]
                left_sum = max(left_sum, temp)

            right_sum = -inf
            temp = 0
            for i in range(mid+1, right+1):
                temp += nums[i]
                right_sum = max(right_sum, temp)

            cross_max = left_sum + right_sum

            return max(left_max, cross_max, right_max)
        
        return helper(0, len(nums)-1)
    

# 1216 ms, 45.94 MB