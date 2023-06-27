class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        lst=[]
        for domainName in cpdomains:
            num,domain=domainName.split(" ")
            domain=domain.split(".")
            for i in range(len(domain)):
                for j in range(i+1,len(domain)):
                    domain[i]+="."+domain[j]
                domain[i]=num+" "+domain[i]
            lst+=domain
        linkDict={}
        for string in lst:
            num,dmn=string.split(" ")
            if dmn in linkDict:
                linkDict[dmn]+=int(num)
            else:
                linkDict[dmn]=int(num)
        lst=[]
        for link in linkDict:
            lst.append(f"{str(linkDict[link])} {link}")
        return lst
