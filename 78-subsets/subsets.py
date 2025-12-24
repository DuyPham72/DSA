class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtrack(temp, start):
            if len(temp) > n:
                return

            ans.append(temp[:])
            for i in range(start, n):
                temp.append(nums[i])
                backtrack(temp, i+1)
                temp.pop()

        backtrack(temp=[], start=0)
        return ans