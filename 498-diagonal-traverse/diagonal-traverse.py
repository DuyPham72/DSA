class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        r, c = 0, 0
        res=[]
        
        for _ in range(m*n):
            res.append(mat[r][c])
            if (r+c)%2==0:
                if c==n-1:
                    r+=1
                elif r==0:
                    c+=1
                else:
                    r-=1
                    c+=1
            else:
                if r==m-1:
                    c+=1
                elif c==0:
                    r+=1
                else:
                    r+=1
                    c-=1
        return res