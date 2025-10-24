from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        if l == 1 or k == 0:
            return nums
        first = nums[:l-k]
        second = nums[-k:]
        nums[:] = second + first