class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2, 3: 3}

        def helper(x):
            if x in memo:
                return memo[x]
            
            memo[x] = helper(x-1) + helper(x-2)
            return memo[x]

        return helper(n)