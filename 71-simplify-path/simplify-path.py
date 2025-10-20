class Solution:
    def simplifyPath(self, path: str) -> str:
        result = path.split('/')
        ans = []

        for p in result:
            if not p or p == '.':
                continue
            elif p == '..':
                if ans:
                    ans.pop()
            else:
                ans.append(p)

        return '/' + '/'.join(ans)