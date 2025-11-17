class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        temp = 0
        first = False
        for i, num in enumerate(nums):
            if first == False and num == 1:
                first = True
                temp = 0
            elif first == True and num == 1:
                if temp-1 < k:
                    return False
                temp = 0
            temp += 1


        return True