class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic=defaultdict(int)
        for c in cpdomains:
            n,link=c.split()
            n=int(n)
            doms=link.split('.')
            if len(doms)==3:
                a,b,c=doms
                dic['.'.join((a,b,c))]+=n
                dic['.'.join((b,c))]+=n
                dic[c]+=n
            else:
                b,c=doms
                dic['.'.join((b,c))]+=n
                dic[c]+=n
        return [f'{num} {d}' for d,num in dic.items()]