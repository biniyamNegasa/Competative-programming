class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ops = set(['+', '*', '-', '/'])
        for token in tokens:
            if token in ops:
                b = stk.pop()
                a = stk.pop()
                if token=='+':
                    stk.append(a+b)
                elif token=='-':
                    stk.append(a-b)
                elif token=='*':
                    stk.append(a*b)
                else:
                    mult = 1
                    if a<0:
                        mult*=-1
                    if b<0:
                        mult*=-1
                    stk.append(mult*(abs(a)//abs(b)))
            else:
                stk.append(int(token))
        return stk.pop()