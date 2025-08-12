class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = 0
        product = 1

        for num in nums:
            if num != 0:
                product *= num
            else:
                zero += 1

        if zero > 1:
            return [0]*len(nums)

        ans = []
        for num in nums:
            if zero == 1:
                if num == 0:
                    ans.append(product)
                else:
                    ans.append(0)
            else:
                ans.append(product//num)

        return ans