class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        temp = prices[0]
        ans = 0
        for price in prices[1:]:
            if price > temp:
                ans += price - temp
                
            temp = price

        return ans