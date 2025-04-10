class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]

        for s in strs:
            if len(s) < len(result):
                result = s

        counter = 0
        while counter < len(result):
            for s in strs:
                if s[counter] != strs[0][counter]:
                    return result[:counter]
            counter += 1

        return result