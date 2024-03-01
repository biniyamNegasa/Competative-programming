# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode], val=0) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return val+root.val
        val += root.val
        return self.sumNumbers(root.left, val*10)+self.sumNumbers(root.right, val*10)