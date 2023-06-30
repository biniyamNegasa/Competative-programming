class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n=len(piles)
        c=0
        for i in range((n//3),n,2):
            c+=piles[i]
        return c
