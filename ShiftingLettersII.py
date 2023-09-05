class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arrToSum=[0]*(len(s)+1)
        for start,end,dxn in shifts:
            if dxn==0:
                arrToSum[start]-=1
                arrToSum[end+1]+=1
            else:
                arrToSum[start]+=1
                arrToSum[end+1]-=1
        curSum=0
        ans=[]
        for i,ch in enumerate(s):
            curSum+=arrToSum[i]
            val=ord(ch)+curSum%26
            if val>122:
                val-=26
            elif val<97:
                val+=26
            ans.append(chr(val))
        return ''.join(ans)
