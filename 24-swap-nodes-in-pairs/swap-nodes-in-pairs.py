# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        node1 = dummy
        while node1.next and node1.next.next:
            curr = node1
            node1 = node1.next
            node2 = node1.next
            after = node2.next

            curr.next = node2
            node2.next = node1
            node1.next = after

        return dummy.next