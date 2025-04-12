class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        row, column = len(matrix), len(matrix[0])
        i, j = 0, 0

        left, right, up, down = 0, 1, 2, 3
        current_direction = right

        top_wall = 0
        right_wall = column
        bot_wall = row
        left_wall = -1

        while len(result) != row*column:
            if current_direction == right:
                while j < right_wall:
                    result.append(matrix[i][j])
                    j += 1
                i, j = i+1, j-1
                right_wall -= 1
                current_direction = down
            elif current_direction == down:
                while i < bot_wall:
                    result.append(matrix[i][j])
                    i += 1
                i, j = i-1, j-1
                bot_wall -= 1
                current_direction = left
            elif current_direction == left:
                while j > left_wall:
                    result.append(matrix[i][j])
                    j -= 1
                i, j = i-1, j+1
                left_wall += 1
                current_direction = up
            else:
                while i > top_wall:
                    result.append(matrix[i][j])
                    i -= 1
                i, j = i+1, j+1
                top_wall += 1
                current_direction = right

        return result