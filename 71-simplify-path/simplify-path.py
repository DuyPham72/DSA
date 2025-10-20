class Solution:
    def simplifyPath(self, path: str) -> str:
        result = re.findall(r'/{1}[a-zA-Z._0-9]+', path)
        ans = []
        
        for p in result:
            if p == '/..':
                if len(ans) > 0:
                    ans.pop() 
                else:
                    continue
            elif p == '/.':
                continue
            else:
                ans.append(p)

        return ''.join(ans) if len(ans) > 0 else '/'