class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dic = {}
        L = 0
        mx = float('-inf')
        tot = 0
        for R in range(len(nums)):
            while nums[R] in dic:
                del dic[nums[L]]
                tot-=nums[L]
                L+=1
            dic[nums[R]]=1
            tot+=nums[R]
            mx = max(mx, tot)
        return mx