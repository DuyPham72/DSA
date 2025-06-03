# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for node in lists:
            while node:
                arr.append(node)
                node = node.next
        arr.sort(key=lambda x: x.val)

        ll = ListNode()
        curr = ll

        for node in arr:
            curr.next = node
            curr = curr.next

        return ll.next