class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        temp = 0

        for letter in s:
            result = False

            for i in range(temp, len(t)):
                if t[i] == letter:
                    temp = i+1
                    result = True
                    break

            if result == False:
                return False

        return True
                