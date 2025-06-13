class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                temp = stack.pop()
                next_greater[temp] = num
            stack.append(num)

        for num in stack:
            next_greater[num] = -1

        return [next_greater[num] for num in nums1]