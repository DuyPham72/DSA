class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cheapest = float('inf')

        for price in prices:
            if price < cheapest:
                cheapest = price
            else:
                profit = max(profit, price - cheapest)

        return profit