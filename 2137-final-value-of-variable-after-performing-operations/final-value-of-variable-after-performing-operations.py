class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for op in operations:
            if op[0] == '-' or op[-1] == '-':
                ans -= 1
            else:
                ans += 1

        return ans