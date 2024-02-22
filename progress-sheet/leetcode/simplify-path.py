class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = [p for p in path.split('/') if p ]
        stk = []
        for p in lst:
            if p=='..':
                if stk:
                    stk.pop()
                continue
            if p=='.':
                continue
            stk.append(p)
        return '/'+ '/'.join(stk)