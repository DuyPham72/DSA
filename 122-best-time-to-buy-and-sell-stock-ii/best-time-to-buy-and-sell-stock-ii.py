class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_price = prices[0]
        max_profit = 0
        temp = 0

        for i in range(n):
            if i < n-1:
                if prices[i] > prices[i+1]:
                    min_price = prices[i+1]
                    max_profit += temp
                    temp = 0
                elif prices[i] < prices[i+1]:
                    temp = max(temp, prices[i+1] - min_price)

        max_profit += temp

        return max_profit