class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])

        edge_set = set()

        def edge_check(i, j, temp):
            if i < 0 or i > row-1 or j < 0 or j > col-1:
                return False
            if board[i][j] == 'X':
                return True

            temp.add((i, j))
            for m, n in [(0,1), (0,-1), (1,0), (-1,0)]:
                x = i+m
                y = j+n
                if (x, y) not in temp:
                    value = edge_check(x, y, temp)
                    if not value:
                        return False

            return True

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O' and (i, j) not in edge_set:
                    temp = set()
                    value = edge_check(i, j, temp) 

                    if value:
                        for x, y in temp:
                            board[x][y] = 'X'
                    else:
                        edge_set.update(temp)