class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for dr in paths:
            p,*f=dr.split()
            for c in f:
                txt,con=c.split("(")
                con=con[:-1]
                dic[con].append(p+'/'+txt)
        ans=[]
        for c in dic:
            if len(dic[c])>1:
                ans.append(dic[c])
        return ans