class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s, t = Counter(s), Counter(t)

        return True if s.items() == t.items() else False