class Solution:
    def freqAlphabets(self, s: str) -> str:
        stk=[]
        dic={str(i):chr(96+i) for i in range(1,10)}
        for i in range(10,27):
            dic[f'{i}#']=chr(96+i)
        i=0
        ans=""
        while i<len(s):
            if int(s[i])>2:
                ans+=dic[s[i]]
                i+=1
            elif i+2<len(s) and s[i+2]=='#':
                ans+=dic[s[i:i+3]]
                i+=3
            else:
                ans+=dic[s[i]]
                i+=1
        return ans
                    