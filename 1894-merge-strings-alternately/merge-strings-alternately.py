class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)

        res = ""

        i = 0
        while i < min(n1, n2):
            res += word1[i]
            res += word2[i]
            i += 1

        res += word1[i:] if n1 > n2 else word2[i:]
        return res