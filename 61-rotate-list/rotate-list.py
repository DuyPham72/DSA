# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        curr = head
        n = 0
        while curr != None:
            n += 1
            curr = curr.next

        dummy = ListNode()
        dummy.next = head

        for i in range(k % n):
            curr = dummy.next
            nextt = curr.next
            while nextt.next != None:
                curr = curr.next
                nextt = nextt.next
            
            curr.next = None
            temp = dummy.next
            dummy.next = nextt
            nextt.next = temp

        return dummy.next