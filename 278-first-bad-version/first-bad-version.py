# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            m = (l+r)//2
            if isBadVersion(m) == False:
                l = m+1
            else:
                if isBadVersion(m-1) == False:
                    return m
                r = m-1

        return l