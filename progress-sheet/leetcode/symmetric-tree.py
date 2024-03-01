# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, curr):
        if not curr:
            return
        return [self.inorder(curr.left), curr.val, self.inorder(curr.right)]
    def revInorder(self, curr):
        if not curr:
            return
        return [self.revInorder(curr.right), curr.val, self.revInorder(curr.left)]

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        print(self.inorder(root.left))
        print(self.inorder(root.right))
        return self.inorder(root.left)==self.revInorder(root.right)
        