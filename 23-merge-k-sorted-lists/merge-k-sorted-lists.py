# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for i, ll in enumerate(lists):
            if ll:
                heapq.heappush(arr, (ll.val, i, ll))

        if not arr:
            return None

        ans = ListNode()
        curr = ans
        while len(arr) > 0:
            value, i, node = heapq.heappop(arr)
            curr.next = node
            curr = curr.next

            node = node.next
            if node:
                heapq.heappush(arr, (node.val, i, node))

        return ans.next