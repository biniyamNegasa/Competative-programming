# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode], mn = float('inf'), mx = float('-inf')) -> int:
        if not root:
            return 0
        left = abs(root.val-mn if mn!=float('inf') else 0)
        right = abs(root.val-mx if mx!=float('-inf') else 0)
        return max(left, right, self.maxAncestorDiff(root.left, min(root.val,mn), max(root.val, mx)), self.maxAncestorDiff(root.right, min(root.val,mn), max(root.val, mx)))