class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        c1 = [0]*26
        c2 = [0]*26
        for c in s1:
            c1[ord(c) - ord('a')] += 1

        window_size = len(s1)
        for i in range(len(s2)):
            c2[ord(s2[i]) - ord('a')] += 1

            if i >= window_size:
                c2[ord(s2[i - window_size]) - ord('a')] -= 1

            if c1 == c2:
                return True

        return False