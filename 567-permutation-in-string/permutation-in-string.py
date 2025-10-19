class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        table = [0]*26
        window = [0]*26
        for i in range(m):
            table[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        if window == table:
            return True

        for i in range(m, n):
            window[ord(s2[i]) - ord('a')] += 1
            window[ord(s2[i-m]) - ord('a')] -= 1

            if window == table:
                return True

        return False