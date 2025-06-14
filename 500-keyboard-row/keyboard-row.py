class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [ set("qwertyuiopQWERTYUIOP"), 
                set("asdfghjklASDFGHJKL"), 
                set("zxcvbnmZXCVBNM")]

        result = []
        for word in words:
            wset = set(word)
            if any(wset <= row for row in rows):
                result.append(word)

        return result                