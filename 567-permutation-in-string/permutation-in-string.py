class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ct = Counter(s1)
        n = len(s1)

        for i, c in enumerate(s2):
            if c in ct and Counter(s2[i:i+n]) == ct:
                return True

        return False