class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        tabulation = [0]*(n+1)
        tabulation[1] = 1
        for i in range(2, n+1):
            tabulation[i] = tabulation[i-1] + tabulation[i-2]

        return tabulation[n]