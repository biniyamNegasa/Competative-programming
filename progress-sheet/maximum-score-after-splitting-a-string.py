class Solution:
    def maxScore(self, s: str) -> int:
        tot = 0
        for ch in s:
            tot+= int(ch)
        zer = 0
        mx = 0
        for ch in s[:-1]:
            if ch=='0':
                zer+=1
            elif ch=='1':
                tot-=1
            mx = max(mx, zer+tot)
        return mx