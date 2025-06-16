class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        up, right, down, left = 0, 1, 2, 3
        direction = right

        top_bound = 0
        right_bound = down_bound = n
        left_bound = -1

        i = j = 0

        ans = [[0 for _ in range(n)] for _ in range(n)]

        for num in range(1, n**2+1):
            ans[i][j] = num

            if direction == right:    
                j += 1
                if j == right_bound:
                    j -= 1
                    i += 1
                    direction = down
                    right_bound -= 1
            elif direction == down:
                i += 1
                if i == down_bound:
                    i -= 1
                    j -= 1
                    direction = left
                    down_bound -= 1
            elif direction == left:
                j -= 1
                if j == left_bound:
                    j += 1
                    i -= 1
                    direction = up
                    left_bound += 1
            else:
                i -= 1
                if i == top_bound:
                    i += 1
                    j += 1
                    direction = right
                    top_bound += 1

        return ans