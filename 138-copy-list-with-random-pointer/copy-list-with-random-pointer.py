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
        for old, new in table.items():
            new_next = table.get(old.next)
            new_random = table.get(old.random)
            new.next = new_next
            new.random = new_random

        return table[head]