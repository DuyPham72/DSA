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
                total = sort[i] + sort[l] + sort[r]
                if total == 0:
                    result.append([sort[i], sort[l], sort[r]])
                    l += 1
                    r -= 1

                    while l < r and sort[l] == sort[l-1]:
                        l+= 1
                    while l < r and sort[r] == sort[r+1]:
                        r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return result