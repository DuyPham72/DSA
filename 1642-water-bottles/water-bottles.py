class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans, empty = numBottles, numBottles
        while empty >= numExchange:
            value, left = divmod(empty, numExchange)
            ans += value
            empty = value + left

        return ans