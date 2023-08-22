class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixSum=[[0]*(len(matrix[0])+1)]
        for i,lst in enumerate(matrix):
            temp=[0,]
            for j,num in enumerate(lst):
                temp.append(num+temp[-1]+self.prefixSum[i][j+1]-self.prefixSum[i][j])
            self.prefixSum.append(temp)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefixSum[row2+1][col2+1]+self.prefixSum[row1][col1]-self.prefixSum[row2+1][col1]-self.prefixSum[row1][col2+1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
