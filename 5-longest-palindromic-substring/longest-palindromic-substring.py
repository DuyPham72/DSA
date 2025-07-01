class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        start = end = 0
        def palindromic(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            return l+1, r-1

        for i in range(n):
            l, r = palindromic(i, i)
            if r-l > end-start:
                start, end = l, r

            l, r = palindromic(i, i+1)
            if r-l > end-start:
                start, end = l, r

        return s[start:end+1]