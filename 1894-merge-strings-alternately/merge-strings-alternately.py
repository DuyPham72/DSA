class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        for count in range(max(len(word1), len(word2))):
            if count < len(word1):
                ans += word1[count]
            if count < len(word2):
                ans += word2[count]

        return ans