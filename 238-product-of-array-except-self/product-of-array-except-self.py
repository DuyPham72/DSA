class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        l_value = 1
        r_value = 1

        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n

        for i in range(n):
            j = -i -1

            l_arr[i] = l_value
            r_arr[j] = r_value

            l_value *= nums[i]            
            r_value *= nums[j]

        for i in range(n):
            answer.append(l_arr[i]*r_arr[i])

        return answer