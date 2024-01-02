class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        arr = [['']*len(strs) for _ in range(len(strs[0]))]
        for i in range(len(strs)):
            for j in range(len(strs[0])):
                arr[j][i] = strs[i][j]
        for chars in arr:
            if ''.join(chars)!=''.join(sorted(chars)):
                count += 1
        return count