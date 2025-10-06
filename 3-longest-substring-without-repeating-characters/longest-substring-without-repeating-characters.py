class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = set()
        longest = 0
        curr = 0
        idx = 0

        for c in s:
            while c in temp:
                temp.remove(s[idx])
                curr -= 1
                idx += 1

            temp.add(c)
            curr += 1
            longest = max(longest, curr)

        return longest