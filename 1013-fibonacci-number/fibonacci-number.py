class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        prev = 0
        curr = 1
        for i in range(2, n+1):
            prev, curr = curr, prev + curr

        return curr