class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = Counter(s)
        T = Counter(t)

        return True if S == T else False