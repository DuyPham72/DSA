class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        position = 0
        for word in s:
            check = False
            for i in range(position, len(t)):
                if t[i] == word:
                    position = i+1
                    check = True
                    break

            if not check:
                return False

        return True