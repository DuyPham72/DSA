class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)

        if n > m:
            small, large = nums2, nums1
        else:
            small, large = nums1, nums2

        result = []
        small_set = set(small)
        for num in large:
            if num in small_set:
                result.append(num)
                small_set.remove(num)

        return result