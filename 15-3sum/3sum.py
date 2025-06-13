class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sort_num = sorted(nums)
        result = []

        for i in range(n):
            if i > 0 and sort_num[i] == sort_num[i-1]:
                continue
            if sort_num[i] > 0:
                break

            l = i+1
            r = n-1
            while l < r:
                total = sort_num[i] + sort_num[l] + sort_num[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    result.append([sort_num[i], sort_num[l], sort_num[r]])
                    l += 1
                    r -= 1
                    while l < r and sort_num[l] == sort_num[l-1]:
                        l += 1
                    while l < r and sort_num[r] == sort_num[r+1]:
                        r -= 1

        return result