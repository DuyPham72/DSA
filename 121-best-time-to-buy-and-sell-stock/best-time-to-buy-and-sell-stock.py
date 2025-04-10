class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        lowest_price = float("inf")

        for price in prices:
            if price < lowest_price:
                lowest_price = price
            elif price > lowest_price:
                profit = max(profit, price - lowest_price)

        return profit