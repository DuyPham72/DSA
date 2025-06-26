class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for s in strs[1:]:
            if len(s) < len(prefix):
                prefix = s

        for s in strs:
            for i in range(len(prefix)):
                if prefix[i] != s[i]:
                    prefix = prefix[:i]
                    break

        return prefix