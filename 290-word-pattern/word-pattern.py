class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False

        temp = {}
        sett = set()
        for w, c in zip(pattern, s.split()):
            if w not in temp and c not in sett:
                sett.add(c)
                temp[w] = c
            else:
                if temp.get(w, None) != c:
                    return False

        return True