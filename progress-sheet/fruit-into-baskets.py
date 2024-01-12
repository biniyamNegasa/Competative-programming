class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = defaultdict(int)
        L = 0
        mx = float('-inf')
        for R in range(len(fruits)):
            while len(dic)==2 and fruits[R] not in dic:
                if dic[fruits[L]]>1:
                    dic[fruits[L]]-=1
                else:
                    del dic[fruits[L]]
                L+=1
            dic[fruits[R]]+=1
            mx = max(mx, R-L+1)
        return mx