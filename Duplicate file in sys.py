class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        m=defaultdict(list)
        for i in paths:
            c=i.split()
            for j in range(1,len(c)):
                a,b=c[j].split('(')
                m[b[:-1]].append(c[0]+'/'+a)
        return [m[i] for i in m if len(m[i])>1]
