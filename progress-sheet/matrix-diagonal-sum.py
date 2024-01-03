class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ssum = 0
        i=0
        j=0
        while i<len(mat) and j<len(mat):
            ssum += mat[i][j]
            i+=1
            j+=1
        j=0
        i-=1
        while i>-1 and j<len(mat):
            ssum += mat[i][j]
            i-=1
            j+=1
        if len(mat)%2:
            m=len(mat)//2
            ssum-=mat[m][m]
        return ssum