class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        temp_pattern = {}
        sett = set()
        new_s = s.split(' ')
        
        if len(pattern) != len(new_s):
            return False

        for w, c in zip(pattern, new_s):
            if w not in temp_pattern and c not in sett:
                sett.add(c)
                temp_pattern[w] = c
            else:
                if temp_pattern.get(w, None) != c:
                    return False

        return True