class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for i in range(n-m+1):
            if haystack[i] == needle[0]:
                temp = 1
                while temp < m and haystack[i+temp] == needle[temp]:
                    temp += 1

                if temp == m:
                    return i

        return -1