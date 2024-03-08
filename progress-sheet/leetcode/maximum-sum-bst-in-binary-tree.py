# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.mx = 0
        def trav(curr):
            if not curr:
                return [0, True, float('-inf'), float('inf')]


            ls,lbs,lmx,lmn = trav(curr.left)
            rs,rbs,rmx,rmn = trav(curr.right)

            if not lbs or not rbs or lmx>=curr.val or curr.val>=rmn:
                return [0, False, curr.val, curr.val]

            self.mx = max(self.mx, curr.val+ls+rs)

            return [curr.val+ls+rs, True, max(rmx, curr.val), min(lmn, curr.val)]

        trav(root)
        return self.mx