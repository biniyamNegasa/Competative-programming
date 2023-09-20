class Solution:
    def timeRequiredToBuy(self, t: List[int], k: int) -> int:
        n=0
        for i,x in enumerate(t):
            n+=min(x,t[k] if i<=k else t[k]-1)
        return n
