# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr.next:
            after = curr.next
            
            a, b = curr.val, after.val
            while b != 0:
                a, b = b, a % b

            node = ListNode(val=a, next=after)
            curr.next = node
            curr = after

        return head