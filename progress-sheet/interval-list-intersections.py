class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        for n in firstList:
            for m in secondList:
                val = []
                val.extend(n)
                val.extend(m)
                val.sort()
                a = val[1]
                b = val[-2]
                if m[0]<=n[1] and n[0]<=m[1]:
                    ans.append([a, b])
        return ans