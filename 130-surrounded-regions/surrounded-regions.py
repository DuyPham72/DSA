class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])

        def edge_cover(i, j):
            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] != 'O':
                return

            board[i][j] = 'D'
            edge_cover(i+1, j)
            edge_cover(i+-1, j)
            edge_cover(i, j+1)
            edge_cover(i, j-1)

        for i in range(row):
            edge_cover(i, 0)
            edge_cover(i, col-1)
        for j in range(col):
            edge_cover(0, j)
            edge_cover(row-1, j)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'D':
                    board[i][j] = 'O'