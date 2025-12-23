class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(start, path):
            # record current subset
            res.append(path[:])

            for i in range(start, n):
                path.append(nums[i])       # choose
                backtrack(i + 1, path)     # explore
                path.pop()                 # un-choose (backtrack)

        backtrack(0, [])
        return res