class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(value):
            hours = 0
            for p in piles:
                hours += ceil(p/value)

            return hours <= h

        r = max(piles)
        l = 1
        while l < r:
            m = (l+r)//2
            if eat(m):
                r = m
            else:
                l = m+1

        return r