class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        def check(time):
            hour = 0
            for p in piles:
                hour += ceil(p/time)

            return hour <= h

        while l < r:
            m = (l+r)//2

            if check(m):
                r = m
            else:
                l = m+1

        return l