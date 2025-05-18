"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        table = {}

        curr = head
        while curr:
            table[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = table[curr]
            copy.next = table.get(curr.next)
            copy.random = table.get(curr.random)  
            curr = curr.next 

        return table[head]