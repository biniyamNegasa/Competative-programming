class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        L = 0
        w_c = 0
        for i in range(k-1):
            if blocks[i]=='W':
                w_c+=1
        mn = float('inf')
        for R in range(k-1, len(blocks)):
            if blocks[R]=='W':
                w_c+=1
            mn = min(mn, w_c)
            if blocks[L]=='W':
                w_c-=1
            L+=1
        return mn