class Solution:
    def doesAliceWin(self, s: str) -> bool:
        temp = set('aeiou')

        for ch in s:
            if ch in temp:
                return True
        return False