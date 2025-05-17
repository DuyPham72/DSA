# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        
        # Move fast ahead by n+1 steps
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both until fast hits the end
        while fast:
            slow = slow.next
            fast = fast.next
        
        # Now slow.next is the node to delete
        to_remove = slow.next
        slow.next = to_remove.next
        # (Optional) clear pointer on removed node
        to_remove.next = None
        
        return dummy.next