# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height = 0

        def length(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = length(node.left)
            right = length(node.right)
            
            self.height = max(self.height, left + right)

            return 1 + max(left, right)

        length(root)

        return self.height