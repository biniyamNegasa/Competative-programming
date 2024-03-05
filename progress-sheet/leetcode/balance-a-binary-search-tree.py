# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left)+[root.val]+self.inorder(root.right)
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = self.inorder(root)
        def build(s, e):
            if s>e:
                return
            mid = (s+e)//2
            curr = TreeNode(nums[mid])
            curr.left = build(s, mid-1)
            curr.right = build(mid+1, e)
            return curr
        return build(0, len(nums)-1)