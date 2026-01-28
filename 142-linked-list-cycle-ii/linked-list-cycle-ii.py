# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        table = {}

        start = head
        while start:
            nextt = start.next
            if nextt in table:
                return nextt
                
            table[start] = nextt
            start = start.next

        return start