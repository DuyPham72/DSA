class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # Start with the first string as the candidate
        prefix = strs[0]

        for word in strs[1:]:
            # Find common length between prefix and word
            i = 0
            max_len = min(len(prefix), len(word))
            while i < max_len and prefix[i] == word[i]:
                i += 1
            # Trim prefix to the matched length
            prefix = prefix[:i]
            # Early exit if nothing is left
            if not prefix:
                break

        return prefix