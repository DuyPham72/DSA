# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = defaultdict(list)
        q = deque([(0, root)])
        while q:
            level, node = q.popleft()
            
            if level not in ans:
                ans[level] = [node.val]
            else:
                ans[level].append(node.val)

            if node.left:
                q.append((level+1, node.left))
            if node.right:
                q.append((level+1, node.right))

        return [i for i in ans.values()]