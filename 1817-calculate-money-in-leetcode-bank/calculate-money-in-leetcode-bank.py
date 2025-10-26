class Solution:
    def totalMoney(self, n: int) -> int:
        week = n // 7
        day = n % 7
        ans = 0

        for i in range(week):
            ans += 28 + i*7

        for i in range(day):
            ans += week + i + 1

        return ans