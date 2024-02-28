# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, curr):
        if not curr:
            return []
        return self.inorder(curr.left)+[curr.val]+self.inorder(curr.right)
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        values = self.inorder(root)
        ans = 0
        for val in values:
            if low<=val<=high:
                ans+=val
        return ans