class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = defaultdict(int)
        for n in arr1:
            dic[n]+=1
        ans = []
        for n in arr2:
            ans.extend(dic[n]*[n])
        ex = []
        for n in dic:
            if n not in arr2:
                ex.extend(dic[n]*[n])
        ex.sort()
        ans.extend(ex)
        return ans