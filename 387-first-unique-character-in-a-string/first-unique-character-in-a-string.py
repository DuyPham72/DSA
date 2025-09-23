class Solution:
    def firstUniqChar(self, s: str) -> int:
        temp = Counter(s)

        for i, value in enumerate(s):
            if temp[value] == 1:
                return i
                
        return -1