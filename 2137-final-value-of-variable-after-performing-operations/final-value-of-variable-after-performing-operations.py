class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for op in operations:
            if op[0] == '-' or op[-1] == '-':
                sign = -1
            else:
                sign = 1

            ans += sign

        return ans