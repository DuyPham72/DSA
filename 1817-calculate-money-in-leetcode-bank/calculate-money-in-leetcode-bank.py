class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        money = 1
        table = {0: 5, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5}

        for i in range(1, n+1):
            if i % 7 == 0:
                money += 1

            ans += money + table[i % 7]

        return ans
