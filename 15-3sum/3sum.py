class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sort = sorted(nums)
        result = []

        for i in range(n):
            if i > 0 and sort[i] == sort[i-1]:
                continue
            if sort[i] > 0:
                break 

            l = i + 1
            r = n-1
            while l < r:
                if sort[i] + sort[l] + sort[r] == 0:
                    result.append([sort[i], sort[l], sort[r]])
                    l += 1
                    r -= 1

                    while l < n and sort[l] == sort[l-1]:
                        l+= 1
                    while r > 0 and sort[r] == sort[r+1]:
                        r -= 1
                elif sort[i] + sort[l] + sort[r] < 0:
                    l += 1
                else:
                    r -= 1

        return result