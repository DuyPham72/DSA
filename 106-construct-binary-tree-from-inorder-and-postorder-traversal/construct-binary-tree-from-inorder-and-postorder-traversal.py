# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hashmap = {val: i for i, val in enumerate(inorder)}

        def build(l_in, r_in, l_post, r_post):
            if l_in >= r_in or l_post >= r_post:
                return

            root_val = postorder[r_post-1]
            node = TreeNode(root_val)

            mid = hashmap[root_val]
            left_side = mid - l_in

            node.left = build(l_in, mid, l_post, l_post + left_side)
            node.right = build(mid+1, r_in, l_post + left_side, r_post-1)

            return node

        n = len(inorder)
        return build(0, n, 0, n)