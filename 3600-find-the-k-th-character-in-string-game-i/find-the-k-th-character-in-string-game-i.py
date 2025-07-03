class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'

        length = 1
        while length < k:
            word = word + ''.join('a' if char == 'z' else chr(ord(char) + 1) for char in word)
            length *= 2

        return word[k-1]