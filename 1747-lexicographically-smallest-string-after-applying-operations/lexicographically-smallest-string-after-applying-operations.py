class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)

        table = {i:str((i+a)%10) for i in range(10)}
        def add(s):
            res = ""
            for i in range(n):
                res += s[i] if i%2 == 0 else table[int(s[i])]
            
            return res

        def rotate(s):
            return s[n-b:] + s[:n-b] 

        ans = set()
        def dfs(s):
            if s in ans:
                return 
            ans.add(s)
            dfs(add(s))
            dfs(rotate(s))
            return

        dfs(s)
        return min(ans)