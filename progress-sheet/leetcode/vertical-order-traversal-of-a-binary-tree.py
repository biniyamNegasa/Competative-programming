# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list)
        def trav(curr, h, i, ans):
            if not curr:
                return
            ans[(h, i)].append(curr.val)
            trav(curr.left, h+1, i-1, ans)
            trav(curr.right, h+1, i+1, ans)
        trav(root, 0, 0, ans)
        for val in ans:
            ans[val].sort()
        real_ans = defaultdict(list)
        for val in sorted(sorted(ans, key=lambda x: x[0]), key=lambda x: x[1]):
            real_ans[val[1]].extend(ans[val])
        return real_ans.values()