class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        start = ['(']
        ans = []

        def trav(i, c, d, curr):
            if len(curr)==2*n:
                ans.append(''.join(curr))
                return
            if len(curr)>2*n:
                return
            if c<n:
                curr.append('(')
                trav(i+1, c+1, d, curr)
                curr.pop()
            if d<c:
                curr.append(')')
                trav(i+1, c, d+1, curr)
                curr.pop()
        trav(0, 1, 0, start)
        return ans