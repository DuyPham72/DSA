class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        temp = {}
        longest = curr_max = l = 0

        for r, char in enumerate(s):
            temp[char] = temp.get(char, 0) + 1
            # curr_max = max(curr_max, temp[char])

            while (r-l+1) - max(temp.values()) > k:
                temp[s[l]] -= 1
                l += 1

            longest = max(longest, r-l+1)

        return longest 