class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        l, r = 0, len(a)-1
        while l < r:
            if a[l] != a[r]:
                return False
            l += 1
            r -= 1
        return True