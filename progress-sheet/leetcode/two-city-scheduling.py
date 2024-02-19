class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        a = 0
        b = 0
        ca = 0
        cb = 0
        costs.sort(key= lambda x:abs(x[0]-x[1]), reverse=True)
        half=len(costs)//2
        for m,n in costs:
            if m>n:
                if cb<half:
                    b+=n
                    cb+=1
                else:
                    a+=m
                    ca+=1
            else:
                if ca<half:
                    a+=m
                    ca+=1
                else:
                    b+=n
                    cb+=1
        return a+b