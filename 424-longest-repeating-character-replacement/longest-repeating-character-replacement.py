class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        temp = {}
        longest = 0
        l = 0

        for r in range(len(s)):
            temp[s[r]] = temp.get(s[r], 0) + 1
            while (r-l+1) - max(temp.values()) > k:
                temp[s[l]] -= 1
                l += 1

            longest = max(longest, (r-l+1))

        return longest