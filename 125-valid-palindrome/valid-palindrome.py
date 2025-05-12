class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(ch for ch in s if ch.isalnum()).lower()

        left = 0
        right = len(clean) - 1

        while left <= right:
            if clean[left] != clean[right]:
                return False
            else:
                left += 1
                right -= 1

        return True