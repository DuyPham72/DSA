class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        for idx, value in enumerate(nums2):
            hashmap[value] = idx
            
        result = []
        for num in nums1:
            ans = -1
            idx = hashmap.get(num)

            for j in range(idx + 1, len(nums2)):
                if num < nums2[j]:
                    ans = nums2[j]
                    break

            result.append(ans)

        return result