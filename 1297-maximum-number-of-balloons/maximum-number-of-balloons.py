class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = 'balloon'
        count = Counter(text)
        ans = []

        for w in word:
            value = count.get(w, 0)

            if w == 'l' or w == 'o':
                ans.append(value//2)
            else:
                ans.append(value)

        return min(ans)