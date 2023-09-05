class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        lst=[]
        n=0
        for p in s:
            if p=='(':
                lst.append(n)
                n=0
            else:
                n=lst.pop()+max(2*n,1)
        return n
