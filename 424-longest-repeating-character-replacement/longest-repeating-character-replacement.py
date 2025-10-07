class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        temp = {}
        longest = 0
        curr_max = 0
        l = 0

        for r in range(len(s)):
            temp[s[r]] = temp.get(s[r], 0) + 1
            curr_max = max(curr_max, temp[s[r]])

            while (r-l+1) - curr_max > k:
                temp[s[l]] -= 1
                l += 1

            longest = max(longest, (r-l+1))

        return longest