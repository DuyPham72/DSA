class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'

        while len(word) < k:
            for w in word:
                value = ord(w) + 1
                if value > ord('z'):
                    word += 'a'
                else:
                    word += chr(value)

        return word[k-1]