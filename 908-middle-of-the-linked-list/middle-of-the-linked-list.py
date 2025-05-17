# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = []

        curr = head

        while curr:
            array.append(curr.val)
            curr = curr.next

        result = head
        for i in range(len(array)//2):
            result = result.next

        return result