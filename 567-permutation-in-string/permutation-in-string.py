class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr = Counter(s1)
        n = len(s1)
        for i, x in enumerate(s2):
            if x in cntr and Counter(s2[i:i+n]) == cntr: return True
        return False