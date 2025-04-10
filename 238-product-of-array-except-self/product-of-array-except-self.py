class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        zero = 0
        product = 1

        for num in nums:
            if num != 0:
                product *= num
            else:
                zero += 1

        if zero == len(nums):
            product = 0

        for num in nums:
            if zero == 0:
                answer.append(int(product/num))
            elif zero == 1 and num == 0:
                answer.append(product)
            else:
                answer.append(0)                

        return answer