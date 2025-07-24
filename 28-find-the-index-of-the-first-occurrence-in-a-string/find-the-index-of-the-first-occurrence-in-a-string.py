class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        temp = len(needle)
        n = len(haystack)

        if temp > n:
            return -1

        for i in range(n - temp + 1):
            if haystack[i:i+temp] == needle:
                return i

        return -1