class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        temp_pattern = {}
        temp_s = {}
        new_s = re.findall(r'[a-z]+', s)
        
        if len(pattern) != len(new_s):
            return False

        for i, w in enumerate(pattern):
            if w not in temp_pattern:
                temp_pattern[w] = new_s[i]
            else:
                if temp_pattern.get(w, None) != new_s[i]:
                    return False

            if new_s[i] not in temp_s:
                temp_s[new_s[i]] = w
            else:
                if temp_s.get(new_s[i], None) != w:
                    return False
        return True