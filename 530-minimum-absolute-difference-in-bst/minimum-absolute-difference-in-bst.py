# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        mindif = [float('inf')]
        temp = [None]

        def dfs(node):
            if not node:
                return 

            dfs(node.left)
            if temp[0] is not None:
                dif = node.val - temp[0]
                if dif < mindif[0]:
                    mindif[0] = dif
            temp[0] = node.val

            dfs(node.right)
        
        dfs(root)
        return mindif[0]