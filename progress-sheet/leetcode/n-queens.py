class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        sum_diagonal,dif_diagonal, clmn = set(), set(), set()
        chess = [['.']*n for _ in range(n)]
        ans = []

        def trav(row):
            if row==n:
                temp = []
                for r in chess:
                    temp.append(''.join(r))
                ans.append(temp)
                return
            for j in range(n):
                if j in clmn or (row+j) in sum_diagonal or (row-j) in dif_diagonal:
                    continue
                clmn.add(j)
                sum_diagonal.add(row+j)
                dif_diagonal.add(row-j)
                chess[row][j] = 'Q'
                trav(row+1)
                chess[row][j] = '.'
                clmn.remove(j)
                sum_diagonal.remove(row+j)
                dif_diagonal.remove(row-j)
        
        trav(0)
        return ans