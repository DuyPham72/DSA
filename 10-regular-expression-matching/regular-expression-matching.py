class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        result = re.findall(p, s)

        return True if s in result else False