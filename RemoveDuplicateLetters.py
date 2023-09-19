class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stk=[]
        dic=Counter(s)
        for ch in s:
            while stk and ch not in stk and stk[-1]>=ch and dic[stk[-1]]>0:
                stk.pop()
            if ch not in stk:
                stk.append(ch)
            dic[ch]-=1
                
        return ''.join(stk)
