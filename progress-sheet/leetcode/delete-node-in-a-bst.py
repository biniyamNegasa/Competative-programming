# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val>key:
            root.left = self.deleteNode(root.left, key)
        elif root.val<key:
            root.right = self.deleteNode(root.right, key)
        else:
            # delete leaf and single child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # has two childs
            successor = root.right

            while successor.left:
                successor = successor.left
            root.val = successor.val

            root.right = self.deleteNode(root.right, successor.val)
        return root
