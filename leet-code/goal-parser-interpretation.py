class Solution:
    def interpret(self, command: str) -> str:
        stk = []
        ans = ""
        for char in command:
            if char=='G':
                ans+=char
            elif char==')':
                if stk:
                    while stk:
                        stk.pop()
                    ans+="al"
                else:
                    ans+='o'
            elif char!='(':
                stk.append(char)
        return ans