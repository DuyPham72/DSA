class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        jewel_set=set(jewels)

        for stone in stones:
            if stone in jewel_set:
                result += 1

        return result