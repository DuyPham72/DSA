# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([(root, 1)])
        ans = 0
        while q:
            node, length = q.pop()

            if not node:
                continue

            ans = max(ans, length)
            q.append((node.left, 1+length))
            q.append((node.right, 1+length))

        return ans