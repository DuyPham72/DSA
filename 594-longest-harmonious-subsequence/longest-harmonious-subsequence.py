class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)

        ans = 0
        for key, value in count.items():
            temp = count.get(key+1, 0)
            if temp:
                ans = max(ans, value + temp)

        return ans