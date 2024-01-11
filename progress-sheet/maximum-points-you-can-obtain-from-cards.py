class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        tot = sum(cardPoints)
        cur = 0
        n = len(cardPoints)
        for i in range(n-k-1):
            cur += cardPoints[i]
        mx = float('-inf')
        L = 0
        if k<n:
            for R in range(n-k-1, n):
                cur += cardPoints[R]
                mx = max(mx, tot-cur)
                cur -= cardPoints[L]
                L+=1
            return mx
        else:
            return tot