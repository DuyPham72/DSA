# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minx = [float('inf')]
        prev = [None]

        def bfs(root):
            if not root:
                return 

            bfs(root.left)

            if prev[0] is not None:
                minx[0] = min(minx[0], root.val - prev[0])
            prev[0] = root.val

            bfs(root.right)

            return

        bfs(root)
        return minx[0]