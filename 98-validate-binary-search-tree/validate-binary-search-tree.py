# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, minx, maxx):
            if not root:
                return True

            if root.val <= minx or root.val >= maxx:
                return False

            return valid(root.left, minx, root.val) and valid(root.right, root.val, maxx)

        return valid(root, float('-inf'), float('inf'))