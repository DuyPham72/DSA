class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        week_money = 1+2+3+4+5+6
        week, day = divmod(n, 7)
        higher, lower = 7, 0

        i = 0
        while i < week:
            week_money += higher - lower
            ans += week_money

            higher += 1
            lower += 1
            i += 1

        for j in range(1, day+1):
            ans += j+i

        return ans