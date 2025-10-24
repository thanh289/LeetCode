from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        nums.reverse()
        nums[:k] = nums[:k][::-1]
        nums[k:l] = nums[k:l][::-1]