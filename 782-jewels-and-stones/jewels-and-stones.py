class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashTable = {}

        for jew in jewels:
            hashTable[jew] = 0

        for stone in stones:
            if stone in hashTable:
                hashTable[stone] += 1

        result = 0

        for key, value in hashTable.items():
            result += value

        return result