# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ll = ListNode()
        curr = ll

        arr = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(arr, (node.val, i, node))

        while len(arr) > 0:
            val, i, node = heapq.heappop(arr)

            curr.next = node
            curr = curr.next

            temp = node.next
            if temp != None:
                heapq.heappush(arr, (temp.val, i, temp))

        return ll.next