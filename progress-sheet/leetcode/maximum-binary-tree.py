# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        dic = {n:i for i, n in enumerate(nums)}
        n = len(nums)
        def rec(s,e):
            if s>e:
                return
            mx = max(nums[s:e+1])
            curr = TreeNode(mx)
            curr.left = rec(s,dic[mx]-1)
            curr.right = rec(dic[mx]+1,e)
            return curr
        return rec(0,n-1)