class Solution:
    def totalNQueens(self, n: int) -> int:
        sum_diagonal, dif_diagonal, clmn = set(), set(), set()
        self.ans = 0
        def trav(row):
            if row==n:
                self.ans+=1
                return 
            for col in range(n):
                if col in clmn or (row+col) in sum_diagonal or (row-col) in dif_diagonal:
                    continue
                clmn.add(col)
                sum_diagonal.add(row+col)
                dif_diagonal.add(row-col)
                trav(row+1)
                clmn.remove(col)
                sum_diagonal.remove(row+col)
                dif_diagonal.remove(row-col)    
        trav(0)
        return self.ans