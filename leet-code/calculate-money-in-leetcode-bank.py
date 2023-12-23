class Solution:
    def totalMoney(self, n: int) -> int:
        val=n//7
        rem=n%7
        ans=0
        s=0
        e=7
        if not val:
            return rem*(rem+1)//2
        for _ in range(val):
            ans+= (e*(e+1)//2) - (s*(s+1)//2)
            s+=1
            e+=1
        if rem:
            e=s+rem
            ans+= (e*(e+1)//2) - (s*(s+1)//2)
        return ans