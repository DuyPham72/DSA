class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for word in strs[1:]:
            n = len(res)
            if n == 0:
                break
            
            count = 0
            m = len(word)
            for i in range(max(n, m)):
                if i < n and i < m and res[i] == word[i]:
                    count += 1
                else:
                    break

            res = res[:count]

        return res