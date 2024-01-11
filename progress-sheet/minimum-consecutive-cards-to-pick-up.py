class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        mn = len(cards)+1
        L = 0
        dic = {}
        for R in range(len(cards)):
            while cards[R] in dic:
                mn = min(mn, R-L+1)
                del dic[cards[L]]
                L+=1
            dic[cards[R]]=1
        return mn if mn!=len(cards)+1 else -1