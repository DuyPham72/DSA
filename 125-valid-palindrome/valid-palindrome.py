class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum()).lower()

        for i in range(len(s)//2):
            if s[i] != s[-i-1]:
                return False

        return True