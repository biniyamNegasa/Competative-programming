class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for ch in s:
            if stk:
                if (ch==']' and stk[-1]=='[') or (ch==')' and stk[-1]=='(') or (ch=='}' and stk[-1]=='{'):
                    stk.pop()
                    continue
            stk.append(ch)
        return not stk