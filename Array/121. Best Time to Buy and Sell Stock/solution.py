from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        result = 0
        for i in range(1, len(prices)):
            if prices[i] <= min_p:
                min_p = prices[i]
            else:
                result = max(result, prices[i] - min_p)
        return result