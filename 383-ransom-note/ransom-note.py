class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter = Counter(magazine)

        for note in ransomNote:
            if note not in letter:
                return False

            if letter[note] == 0:
                return False
                
            letter[note] -= 1

        return True