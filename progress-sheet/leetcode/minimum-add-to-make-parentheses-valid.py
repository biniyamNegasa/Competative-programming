class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []
        for ch in s:
            if ch==')' and stk and stk[-1]=='(':
                stk.pop()
            else:
                stk.append(ch)
        return len(stk)