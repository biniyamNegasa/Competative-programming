# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(curr, ans):
            if not curr:
                return
            ans[curr.val]+=1
            inorder(curr.left, ans)
            inorder(curr.right, ans)
            return ans
        ans = inorder(root, defaultdict(int))
        res = set()
        ans_sorted = sorted(ans, key=lambda x: ans[x], reverse=True)
        compare = ans[ans_sorted[0]]
        for val in ans_sorted:
            if ans[val]==compare:
                res.add(val)
            else:
                break
        return res