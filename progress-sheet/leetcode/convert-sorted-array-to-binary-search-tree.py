# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def binary(s,e):
            if s>e:
                return
            mid = (s+e)//2
            curr = TreeNode(nums[mid])
            curr.left = binary(s,mid-1)
            curr.right = binary(mid+1, e)
            return curr
        n = len(nums)
        return binary(0, n-1)