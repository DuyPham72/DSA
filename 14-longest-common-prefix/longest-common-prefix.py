class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for word in strs[1:]:
            n = len(res)
            if n == 0:
                break
            
            m = len(word)
            for i in range(max(n, m)):
                if i >= n or i >= m or res[i] != word[i]:
                    res = res[:i]
                    break

        return res