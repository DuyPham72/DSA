class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = Counter(s)
        T = Counter(t)

        return True if S.items() == T.items() else False