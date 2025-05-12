class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            column = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in row:
                    return False

                if board[j][i] != "." and board[j][i] in column:
                    return False

                row.add(board[i][j])
                column.add(board[j][i])

        for box_row in (0, 3, 6):
            for box_col in (0, 3, 6):
                seen_box = set()
                for i in range(3):
                    for j in range(3):
                        cell = board[box_row + i][box_col + j]

                        if cell != "." and cell in seen_box:
                            return False

                        seen_box.add(cell)

        return True