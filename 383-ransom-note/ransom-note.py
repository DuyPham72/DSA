class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)

        for word in ransomNote:
            if count.get(word, 0) == 0:
                return False
            
            count[word] -= 1

        return True