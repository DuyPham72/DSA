class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        distinct = set(jewels)
        ans = 0
        for stone in stones:
            if stone in distinct:
                ans += 1

        return ans