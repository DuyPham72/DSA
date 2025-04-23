class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = Counter(s)
        T = Counter(t)

        if S.items() == T.items():
            return True
        return False