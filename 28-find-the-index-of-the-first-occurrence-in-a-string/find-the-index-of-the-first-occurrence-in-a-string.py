class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for i in range(n):
            if haystack[i] == needle[0]:
                temp = 1
                while i+temp < n and temp < m:
                    if haystack[i+temp] != needle[temp]:
                        break

                    temp += 1

                if temp == m:
                    return i

        return -1