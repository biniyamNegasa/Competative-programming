class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        minSP=[]
        prev=[]
        minSN=[]
        n=len(arr)
        nxt=[n]*n
        tot=0
        for i,x in enumerate(arr):
            while minSP and arr[minSP[-1]]>x:
                minSP.pop()
            prev.append(minSP[-1] if minSP else -1)
            minSP.append(i)
            while minSN and arr[minSN[-1]]>x:
                nxt[minSN.pop()]=i
            minSN.append(i)
        for i,x in enumerate(arr):
            tot+=x*(i-prev[i])*(nxt[i]-i)
        return tot%(10**9+7)
