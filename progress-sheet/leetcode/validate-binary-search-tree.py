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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = self.inorder(root)
        n = len(ans)
        if n==1:
            return True
        for i in range(n-1):
            if ans[i]>=ans[i+1]:
                return False
        return True