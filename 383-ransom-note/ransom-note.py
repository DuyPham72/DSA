class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter = Counter(magazine)

        for note in ransomNote:
            if note not in letter:
                return False
            elif letter[note] == 0:
                return False
            else:
                letter[note] -= 1

        return True