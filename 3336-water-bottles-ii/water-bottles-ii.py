class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans, empty = numBottles, numBottles
        while empty >= numExchange:
            value, left = divmod(empty, numExchange)
            print(value, left)
            ans += 1
            empty = (value-1)*numExchange + left + 1
            numExchange += 1
            print(empty)

        return ans