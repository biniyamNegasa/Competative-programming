class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        mn = min(costs)
        mx = max(costs)
        arr = [0]*(mx-mn+1)
        for n in costs:
            arr[n-mn]+=1
        j=0
        for i, n in enumerate(arr):
            while n:
                costs[j]=mn+i
                j+=1
                n-=1
        ans = 0
        count = 0
        for cost in costs:
            if ans+cost<=coins:
                ans+=cost
                count+=1
        return count