class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        else:
            i, j = 0, 0

            while j < len(nums2):
                if nums1[i] == 0:
                    nums1[i] = nums2[j]
                    j += 1
                i += 1

            nums1.sort()
