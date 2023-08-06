class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1D={}
        for alp in s1:
            if alp in s1D:
                s1D[alp]+=1
            else:
                s1D[alp]=1
        start=0
        end=len(s1)
        while end<len(s2)+1:
            s2D={}
            for alp in s2[start:end]:
                if alp in s2D:
                    s2D[alp]+=1
                else:
                    s2D[alp]=1
            if s1D==s2D:
                return True
            start+=1
            end+=1
        return False
