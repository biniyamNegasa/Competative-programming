class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s=[*s]
        p=sorted([*p])
        arr=[]
        start=0
        end=len(p)
        while end<len(s)+1:
            b=sorted(s[start:end])
            if p==b:
                arr.append(start)
            start+=1
            end+=1
        return arr
