class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        temp = len(needle)
        n = len(haystack)

        if temp > n:
            return -1

        for i in range(n):
            if haystack[i] == needle[0]:
                ans = i
                for j in range(temp):
                    if i+j >= n or haystack[i+j] != needle[j]:
                        ans = -1
                        break

                if ans != -1:
                    return ans

        return -1