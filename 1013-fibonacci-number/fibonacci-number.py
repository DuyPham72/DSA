class Solution:
    def fib(self, n: int) -> int:
        memo= {}
        memo[0] = 0
        memo[1] = 1

        def dp(x):
            if x in memo:
                return memo[x]
            
            memo[x] = dp(x-1) + dp(x-2)
            return memo[x]

        return dp(n)
            