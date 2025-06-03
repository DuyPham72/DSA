class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        arr = [0] * (n+1)

        for num, freq in counter.items():
            if arr[freq] == 0:
                arr[freq] = [num]
            else:
                arr[freq].append(num)

        result = []
        for i in range(n, -1, -1):
            if arr[i] != 0:
                result.extend(arr[i])
            if len(result) == k:
                break

        return result