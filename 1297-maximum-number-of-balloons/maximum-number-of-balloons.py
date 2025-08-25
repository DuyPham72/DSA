class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = "balloon"
        T = Counter(text)
        temp = []

        for c in word:
            value = T.get(c, 0)
            if c == 'l' or c == 'o':
                temp.append(value//2)
            else:
                temp.append(value)

        return min(temp)