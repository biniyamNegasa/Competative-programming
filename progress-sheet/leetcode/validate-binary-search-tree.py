# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], mn=float('-inf'), mx=float('inf')) -> bool:
        if not root:
            return True
        if root.val<=mn or root.val>=mx:
            return False
        return self.isValidBST(root.left, mn, root.val) and self.isValidBST(root.right, root.val, mx)