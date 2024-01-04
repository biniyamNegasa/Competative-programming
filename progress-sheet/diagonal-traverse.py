class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                dic[i+j].append(mat[i][j])
        diag_list = []
        for n in dic:
            if n%2:
                diag_list.extend(dic[n])
            else:
                diag_list.extend(dic[n][::-1])
        return diag_list