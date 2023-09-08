class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps={}
        stk=[]
        ans=0
        mx=0
        for i,e in enumerate(position):
            ps[e]=i
        for e in ps:
            ps[e]=speed[ps[e]]
        for e in sorted(ps,reverse=True):
            data=(target-e)/ps[e]
            if not stk:
                stk.append(data)
                mx=data
            else:
                if data>mx:
                    while stk:
                        stk.pop()
                    ans+=1
                    mx=0
                stk.append(data)
                mx=max(mx,data)
        if stk:
            ans+=1
        return ans
