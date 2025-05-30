# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kth = [k]
        result = [0]

        def bfs(root):
            if not root:
                return 

            bfs(root.left)

            if kth[0] == 1:
                result[0] = root.val

            kth[0] = kth[0] - 1
            if kth[0] > 0:
                bfs(root.right)

            return 

        bfs(root)
        return result[0]