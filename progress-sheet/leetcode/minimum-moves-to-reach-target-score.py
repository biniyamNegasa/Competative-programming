class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        db = 0
        tot_rem = 0
        while target>1 and maxDoubles:
            tot_rem+= target%2
            target//=2
            maxDoubles-=1
            db+=1
        return target-1+tot_rem+db