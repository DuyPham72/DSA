class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []

        def backtracking(x=0):
            if x == len(nums):
                ans.append(temp.copy())
                return

            backtracking(x+1)

            temp.append(nums[x])
            backtracking(x+1)
            temp.pop()

        backtracking()
        return ans