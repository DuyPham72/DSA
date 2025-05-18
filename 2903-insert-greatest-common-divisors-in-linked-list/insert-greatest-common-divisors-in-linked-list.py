# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            after = curr.next
            
            result = math.gcd(curr.val, after.val)
            temp = ListNode(result)

            curr.next = temp
            temp.next = after
            curr = after

        return head 