# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        ans = [[root.val]]
        i = 1
        while q:
            sz = len(q)
            temp = []
            for _ in range(sz):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                    temp.append(curr.left.val)
                if curr.right:
                    q.append(curr.right)
                    temp.append(curr.right.val)
            if i%2:
                temp.reverse()
            ans.append(temp)
            i+=1
        ans.pop()
        return ans