# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def insert(curr, node):
            if not curr:
                return
            if curr.val>node.val:
                if not curr.left:
                    curr.left = node
                    return
                insert(curr.left, node)
            else:
                if not curr.right:
                    curr.right = node
                    return
                insert(curr.right, node)
        insert(root, TreeNode(val))
        return root