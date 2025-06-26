class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]

        for word in strs[1:]:
            min_length = min(len(ans), len(word))
            i = 0
            while i < min_length and ans[i] == word[i]:
                i += 1

            ans = ans[:i]
            if len(ans) == 0:
                break

        return ans