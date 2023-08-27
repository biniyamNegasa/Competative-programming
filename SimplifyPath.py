class Solution:
    def simplifyPath(self, path: str) -> str:
        ans=[]
        s=path.split('/')
        for ch in s:
            if ans and ch=='..':
                ans.pop()
            elif ch=='' or ch=='.' or ch=='..':
                continue
            else:
                ans.append(ch)
        return '/'+'/'.join(ans)
