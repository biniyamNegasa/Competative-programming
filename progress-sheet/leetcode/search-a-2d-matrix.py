class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        clmn = len(matrix[0])
        left = 0
        right = row*clmn-1
        while left<=right:
            mid = (left+right)//2
            r = mid//clmn
            c = mid%clmn
            if matrix[r][c]>target:
                right = mid-1
            elif matrix[r][c]<target:
                left = mid+1
            else:
                return True
        return False