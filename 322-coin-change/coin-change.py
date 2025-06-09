class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo = {0:0}

        def f(x):
            if x in memo:
                return memo[x]

            minn = float('inf')
            for coin in coins:
                dif = x - coin
                if dif < 0:
                    break
                
                minn = min(minn, 1 + f(dif))

            memo[x] = minn
            return memo[x]

        result = f(amount)
        return result if result < float('inf') else -1