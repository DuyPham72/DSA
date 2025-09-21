class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        temp_pattern = {}
        sett = set()
        
        if len(pattern) != len(s.split()):
            return False
 
        for w, c in zip(pattern, s.split()):
            if w not in temp_pattern and c not in sett:
                sett.add(c)
                temp_pattern[w] = c
            else:
                if temp_pattern.get(w, None) != c:
                    return False

        return True