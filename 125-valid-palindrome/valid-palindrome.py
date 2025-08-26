class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        letters = re.findall(f"[a-z0-9]",s)
        new_s = ''.join(letters)
        print(new_s)
        
        n = len(new_s)
        for i in range(n//2):
            if new_s[i] != new_s[-i-1]:
                return False

        return True