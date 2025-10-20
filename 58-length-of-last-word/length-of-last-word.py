class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.lstrip().rstrip()
        ans = ''
        for c in s[::-1]:
            if c != ' ':
                ans += c
            else:
                break

        return len(ans)