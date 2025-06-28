# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hashmap = {val:i for i, val in enumerate(postorder)}

        def builder(l_pre, r_pre, l_post, r_post):
            if l_pre >= r_pre or l_post >= r_post:
                return

            root_val = preorder[l_pre]
            node = TreeNode(root_val)

            if r_pre - l_pre == 1:
                return node

            left_node = preorder[l_pre+1]
            
            mid = hashmap[left_node]
            left_side = mid - l_post + 1 

            node.left = builder(l_pre + 1, l_pre + 1 + left_side, l_post, mid+1)
            node.right = builder(l_pre + 1 + left_side, r_pre, mid+1, r_post-1)

            return node

        n = len(preorder)
        return builder(0, n, 0, n)