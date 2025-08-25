class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                if board[i][j] in row or board[j][i] in col:
                    return False

                if board[i][j] != '.': row.add(board[i][j])
                if board[j][i] != '.': col.add(board[j][i])

        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                box = set()

                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y] in box:
                            return False

                        if board[i+x][j+y] != '.': box.add(board[i+x][j+y])

        return True