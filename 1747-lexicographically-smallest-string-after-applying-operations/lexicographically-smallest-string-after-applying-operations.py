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

        seen = set([s])
        q = deque([s])
        smallest = s

        while q:
            cur = q.popleft()
            if cur < smallest:
                smallest = cur

            # Operation 1: add
            added = add(cur)
            if added not in seen:
                seen.add(added)
                q.append(added)

            # Operation 2: rotate
            rotated = rotate(cur)
            if rotated not in seen:
                seen.add(rotated)
                q.append(rotated)

        return smallest