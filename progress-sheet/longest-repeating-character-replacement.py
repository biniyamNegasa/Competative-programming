class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mx = 0
        for i in range(65, 91):
            mx = max(mx, self.larger(s, k, chr(i)))
        return mx
    
    def larger(self, s: str, k: int, ch: str) -> int:
        mx = 0
        
        L = 0
        for R in range(len(s)):
            while not k and s[R]!=ch:
                if s[L]!=ch:
                    k+=1
                L+=1
            if s[R]!=ch:
                k-=1
            mx = max(mx, R-L+1)
        return mx