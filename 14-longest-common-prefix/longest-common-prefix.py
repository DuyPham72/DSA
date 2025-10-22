class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for word in strs[1:]:
            if len(word) < len(ans):
                ans = word

        for word in strs:
            if len(ans) == 0:
                return ''

            for i in range(min(len(ans), len(word))):
                if ans[i] != word[i]:
                    ans = word[:i]
                    break

        return ans