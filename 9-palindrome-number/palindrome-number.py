class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)
        return True if temp == temp[::-1] else False