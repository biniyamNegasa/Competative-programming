class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        ops='+*-/'
        for num in tokens:
            if num in ops:
                b=stack.pop()
                a=stack.pop()
                c=0
                if num=='+':
                    c=a+b
                elif num=='-':
                    c=a-b
                elif num=='*':
                    c=a*b
                else:
                    c=int(a/b)
                stack.append(c)
            else:
                stack.append(int(num))
        return stack.pop()
