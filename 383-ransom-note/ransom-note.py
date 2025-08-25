class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        temp = Counter(magazine)

        for c in ransomNote:
            value = temp.get(c, 0)
            if value == 0:
                return False

            temp[c] -= 1

        return True