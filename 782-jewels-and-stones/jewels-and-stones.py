class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        Stones = Counter(stones)
        Jewels = set(jewels)

        result = 0
        for key, value in Stones.items():
            if key in Jewels:
                result += value

        return result