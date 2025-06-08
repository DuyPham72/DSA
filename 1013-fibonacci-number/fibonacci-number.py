class Solution:
    def fib(self, n: int) -> int:
        memorization = {}
        memorization[0] = 0
        memorization[1] = 1

        if n in memorization:
            return memorization[n]

        for i in range(2, n+1):
            memorization[i] = memorization[i-1] + memorization[i-2]

        return memorization[n]