class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        pre_sum = [0]*(n+1)
        for a, b in requests:
            pre_sum[a]+=1
            pre_sum[b+1]-=1
        pre_sum.pop()
        nums.sort()
        for i in range(1, n):
            pre_sum[i]+=pre_sum[i-1]
        pre_sum.sort()
        ans = 0
        curr = 0
        for i in range(n-1,-1,-1):
            ans += pre_sum[i]*nums[i]
        return ans%(10**9 +7)