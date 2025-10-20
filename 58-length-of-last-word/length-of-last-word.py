class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        ans = 0
        for c in s[::-1]:
            if c != ' ':
                ans += 1
            else:
                return ans

        return ans