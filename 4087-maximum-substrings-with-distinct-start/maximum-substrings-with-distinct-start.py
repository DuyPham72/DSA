class Solution:
    def maxDistinct(self, s: str) -> int:
        letter_count = Counter(s)
        return len(letter_count.keys())