class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        L={}
        W={}
        
        for w,l in matches:
            L[l]=L.get(l,0)+1
            W[w]=W.get(w,0)+1
        one=[]
        for l in L:
            if L[l]==1:
                one.append(l)
        zero=[]
        for w in W:
            if w not in L:
                zero.append(w)
        return [sorted(zero),sorted(one)]