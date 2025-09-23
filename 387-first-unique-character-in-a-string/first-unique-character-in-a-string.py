class Solution:
    def firstUniqChar(self, s: str) -> int:
        temp = Counter(s)

        value = None
        for key, value in temp.items():
            if value == 1:
                value = key
                break

        for i in range(len(s)):
            if s[i] == value:
                return i

        return -1