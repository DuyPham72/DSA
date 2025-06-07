"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        g = {}
        start = node
        seen = set()
        seen.add(start)
        stack = [start]

        while stack:
            node = stack.pop()
            g[node] = Node(node.val)

            for nei in node.neighbors:
                if nei not in seen:
                    seen.add(nei)
                    stack.append(nei)

        for old, new in g.items():
            for nei in old.neighbors:
                new_nei = g[nei]
                new.neighbors.append(new_nei)

        return g[start]