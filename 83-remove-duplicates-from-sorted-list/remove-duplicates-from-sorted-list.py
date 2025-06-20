# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        curr = head
        while curr.next:
            after = curr.next
            if after.val == curr.val:
                curr.next = after.next
            else:
                curr = curr.next

        return head