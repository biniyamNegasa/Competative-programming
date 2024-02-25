class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        for ch in s:
            if ch==')':
                val = 0
                if stk and stk[-1]!='(':
                    while stk and stk[-1]!='(':
                        val+=stk.pop()
                stk.pop()
                if val:
                    stk.append(2*val)
                else:
                    stk.append(1)
            else:
                stk.append(ch)
        ans = 0
        while stk:
            ans += stk.pop()
        return ans