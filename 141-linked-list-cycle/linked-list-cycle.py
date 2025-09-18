# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        curr1 = head
        curr2 = head.next

        while curr2 and curr2.next:
            if curr1 is curr2:
                return True

            curr1 = curr1.next
            curr2 = curr2.next.next

        return False