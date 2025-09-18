class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)
        empty = []

        for i in range(9):
            for j in range(9):
                value = board[i][j]

                if board[i][j] != '.':
                    row[i].add(value)
                    col[j].add(value)
                    box[(i//3, j//3)].add(value)
                else:
                    empty.append((i, j))

        def dfs(idx):
            if idx == len(empty):
                return True 

            r, c = empty[idx]
            for digit in map(str, range(1, 10)):
                if digit not in row[r] and digit not in col[c] and digit not in box[(r // 3, c // 3)]:
                    board[r][c] = digit
                    row[r].add(digit)
                    col[c].add(digit)
                    box[(r // 3, c // 3)].add(digit)

                    if dfs(idx + 1):
                        return True

                    board[r][c] = '.'
                    row[r].remove(digit)
                    col[c].remove(digit)
                    box[(r // 3, c // 3)].remove(digit)

            return False 

        dfs(0)