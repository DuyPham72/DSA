class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        temp_pattern = {}
        temp_s = {}
        new_s = s.split(' ')
        
        if len(pattern) != len(new_s):
            return False

        for w, c in zip(pattern, new_s):
            if w not in temp_pattern:
                temp_pattern[w] = c
            else:
                if temp_pattern.get(w, None) != c:
                    return False

            if c not in temp_s:
                temp_s[c] = w
            else:
                if temp_s.get(c, None) != w:
                    return False
        return True