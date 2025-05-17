# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        temp = set()

        curr = head

        while curr.next:
            if curr not in temp:
                temp.add(curr)
            else:
                return True
            curr = curr.next

        return False