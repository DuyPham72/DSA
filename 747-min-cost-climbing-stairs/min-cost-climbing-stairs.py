class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 2:
            return min(cost)

        prev = 0
        curr = 0
        for i in range(2, n+1):
            temp = curr
            curr = min(cost[i-1] + curr, cost[i-2] + prev)
            prev = temp

        return  curr