class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_check(k):
            hours = 0
            for p in piles:
                hours += ceil(p/k)
            
            return hours <= h

        l = 1
        r = max(piles)

        while l < r:
            m = l + ((r-l) // 2)
            if k_check(m):
                r = m
            else:
                l = m+1

        return r