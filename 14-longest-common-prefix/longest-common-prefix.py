class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for word in strs[1:]:
            if len(word) < len(res):
                res = word

        for word in strs:
            for i in range(len(res)):
                if res[i] != word[i]:
                    res = res[:i]
                    break 

        return res