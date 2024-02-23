class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key= lambda x: abs(x[0]-x[1]), reverse=True)
        n = len(costs)//2
        a, b, ca, cb = 0, 0, 0, 0
        for x,y in costs:
            if x<y:
                if ca<n:
                    a+=x
                    ca+=1
                else:
                    b+=y
                    cb+=1
            else:
                if cb<n:
                    b+=y
                    cb+=1
                else:
                    a+=x
                    ca+=1
        return a+b