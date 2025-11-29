# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.value = k
        self.ans = None

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)

            if self.value == 1:
                self.ans = node.val
            self.value -= 1

            dfs(node.right)

        dfs(root)
        return self.ans