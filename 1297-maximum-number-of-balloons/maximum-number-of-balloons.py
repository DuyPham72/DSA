class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        table = Counter(text)
        balloon = Counter("balloon")
        
        return min(table[ch] // balloon[ch] for ch in balloon)