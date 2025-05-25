# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        def compare(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False

            if root1.val != root2.val:
                return False

            return compare(root1.left, root2.left) and compare(root1.right, root2.right)

        if not root:
            return False

        if root.val == subRoot.val:
            value = compare(root, subRoot)
            if value == True:
                return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right