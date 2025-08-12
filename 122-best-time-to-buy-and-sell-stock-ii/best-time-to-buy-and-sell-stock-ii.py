class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = float('inf')

        for num in prices:
            if num >= buy:
                res += num - buy
            buy = num

        return res