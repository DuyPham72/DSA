class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []

        zero_count = 0
        product_without_zero = 1
        for num in nums:
            if num != 0:
                product_without_zero *= num
            else:
                zero_count += 1

        for num in nums:
            if zero_count == 0:
                ans.append(product_without_zero//num)
            elif zero_count == 1:
                if num == 0:
                    ans.append(product_without_zero)
                else:
                    ans.append(0)
            else:
                return [0]*len(nums)

        return ans