class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = (l+r)//2

            hours = 0
            for p in piles:
                hours += ceil(p/m)

            value = True if hours <= h else False
            if value:
                r = m
            else:
                l = m+1

        return r