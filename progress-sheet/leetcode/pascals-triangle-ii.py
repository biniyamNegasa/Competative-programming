class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        ans = []
        arr = self.getRow(rowIndex-1)
        for i in range(len(arr)-1):
            ans.append(arr[i]+arr[i+1])
        return [1]+ans+[1]