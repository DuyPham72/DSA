# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        while l1:
            num1 += str(l1.val)
            l1 = l1.next

        num2 = ""
        while l2:
            num2 += str(l2.val)
            l2 = l2.next

        num1 = num1[::-1]
        num2 = num2[::-1]
        result = str(int(num1) + int(num2))
        result = result[::-1]

        dummy = ListNode()
        curr = dummy
        for c in result:
            temp = ListNode(int(c))
            curr.next = temp
            curr = curr.next

        return dummy.next