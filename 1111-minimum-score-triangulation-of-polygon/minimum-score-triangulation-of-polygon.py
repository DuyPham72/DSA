class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0]*n for _ in range(n)]
        
        for l in range(2, n+1): # length of sub-polygon
            for i in range(n-l):
                j = i + l
                dp[i][j] = float('inf')
                for k in range(i+1, j): # try splitting at k
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + values[i]*values[j]*values[k])

        return dp[0][n-1]