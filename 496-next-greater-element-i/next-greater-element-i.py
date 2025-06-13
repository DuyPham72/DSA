class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in range(len(nums1)):
            ans = -1
            idx = 0
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    idx = j

            for j in range(idx+1, len(nums2)):
                if nums1[i] < nums2[j]:
                    ans = nums2[j]
                    break

            result.append(ans)

        return result