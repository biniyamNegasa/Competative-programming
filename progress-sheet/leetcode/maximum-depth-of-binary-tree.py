# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = []
        def trav(node, val):
            if not node:
                ans.append(val)
                return
            trav(node.left, val+1)
            trav(node.right, val+1)
        trav(root, 0)
        return max(ans)