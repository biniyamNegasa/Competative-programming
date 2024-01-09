class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        dic_s1 = Counter(s1)
        L = 0
        dic_s2 = defaultdict(int)
        for i in range(len(s1)-1):
            dic_s2[s2[i]]+=1
        for R in range(len(s1)-1, len(s2)):
            dic_s2[s2[R]]+=1
            if dic_s1==dic_s2:
                return True
            if dic_s2[s2[L]]>1:
                dic_s2[s2[L]]-=1
            else:
                del dic_s2[s2[L]]
            L+=1
        return False