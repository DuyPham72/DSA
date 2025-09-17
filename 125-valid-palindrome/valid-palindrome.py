class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = re.findall(f'[a-z0-9]', s.lower())
        s = ''.join(alphanumeric)

        for i in range(len(s)//2):
            if s[i] != s[-i-1]:
                return False

        return True