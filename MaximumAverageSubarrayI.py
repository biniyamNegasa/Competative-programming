class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        preSum=[0]
        for num in nums:
            preSum.append(preSum[-1]+num)
        maxAv=-10001
        s=0
        e=k-1
        while e<len(nums):
            a=preSum[e+1]-preSum[s]
            if a/k>maxAv:
                maxAv=a/k
            s+=1
            e+=1
        return maxAv
            
