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
        oldtoNew = {}

        def dfs(node):
            if node in oldtoNew:        # return copy if its there
                return oldtoNew[node]
            
            copy = Node(node.val)       # create copy then add to dict
            oldtoNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))   # recursively call for nbr, append copy (result of dfs()) to cur.nbrs
            
            return copy
        
        return dfs(node) if node else None