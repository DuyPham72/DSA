class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)

        ans = ''
        for count in range(max(len1, len2)):
            if count < len1:
                ans += word1[count]
            if count < len2:
                ans += word2[count]

        return ans