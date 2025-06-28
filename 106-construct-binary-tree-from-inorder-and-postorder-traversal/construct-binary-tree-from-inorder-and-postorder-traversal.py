# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        hashmap = {val: i for i, val in enumerate(inorder)}

        def helper(l_in, r_in, l_post, r_post):
            if l_in >= r_in or l_post >= r_post:
                return

            root_node = postorder[r_post - 1]
            node = TreeNode(root_node)

            mid = hashmap[root_node]
            left_side = mid - l_in

            node.left = helper(l_in, mid, l_post, l_post + left_side)
            node.right = helper(mid+1, r_in, l_post + left_side, r_post-1)

            return node

        return helper(0, n, 0, n)