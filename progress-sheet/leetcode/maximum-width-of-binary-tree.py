# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        mx = 1
        ind = 1
        val = deque([1])
        while q:
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                v = val.popleft()
                if curr.left:
                    q.append(curr.left)
                    val.append(2*v)
                if curr.right:
                    q.append(curr.right)
                    val.append(2*v + 1)
            if val:
                mx = max(mx, val[-1]-val[0]+1)
        return mx