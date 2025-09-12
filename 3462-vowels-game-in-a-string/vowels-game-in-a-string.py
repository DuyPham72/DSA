class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for ch in s:
            if ch in set('aeiou'):
                return True
        return False