class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        n = len(s1)
        c1 = Counter(s1)
        c2 = {}

        for i in range(n):
            if s2[i] in c2:
                c2[s2[i]] += 1
            else:
                c2[s2[i]] = 1
        if c1 == c2:
                return True

        for i in range(n, len(s2)):
            if s2[i] in c2:
                c2[s2[i]] += 1
            else:
                c2[s2[i]] = 1
            
            c2[s2[i-n]] -= 1
            if c2[s2[i-n]] == 0:
                del c2[s2[i-n]]

            if c1 == c2:
                return True

        return False