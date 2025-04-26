class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        table = Counter(text)
        word = "balloon"
        require = Counter(word)
        
        result = []

        for char in word:
            if char not in table:
                return 0

            result.append(table[char] // require[char])

        return min(result)