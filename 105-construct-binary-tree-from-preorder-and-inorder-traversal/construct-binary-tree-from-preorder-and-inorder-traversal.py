# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {val:i for i, val in enumerate(inorder)}

        def build(l_pre, r_pre, l_in, r_in):
            if l_pre >= r_pre or l_in >= r_in:
                return

            root_val = preorder[l_pre]
            node = TreeNode(root_val)

            mid = hashmap[root_val]
            left_side = mid - l_in

            node.left = build(l_pre + 1, l_pre + 1 + left_side, l_in, mid)
            node.right = build(l_pre + 1 + left_side, r_pre, mid+1, r_in)

            return node

        n = len(inorder)
        return build(0, n, 0, n)