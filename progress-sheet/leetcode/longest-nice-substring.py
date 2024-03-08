class Solution:
    def isNice(self, s):
        count = Counter(s)
        for ch in count:
            if ch.lower() not in count or ch.upper() not in count:
                return False
        return True
    def longestNiceSubstring(self, s: str) -> str:
        self.ans = ''
        n = len(s)
        def trav(i):
            if i==n:
                return 
            for j in range(i+1, n):
                chrs = s[i:j+1]
                if self.isNice(chrs) and len(chrs)>len(self.ans):
                    self.ans = chrs
            trav(i+1)
        trav(0)
        return self.ans