class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic={}
        mx=0
        pmx=-1
        ans=[]
        for i,char in enumerate(s):
            dic[char]=i
        for i,char in enumerate(s):
            mx=max(mx,dic[char])
            if mx==i:
                ans.append(mx-pmx)
                pmx=mx
        return ans
