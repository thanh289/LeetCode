from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        no_zero = [x for x in nums if x != 0]
        nums[:] = no_zero + [0] * (len(nums) - len(no_zero))