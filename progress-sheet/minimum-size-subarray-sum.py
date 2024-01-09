class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mn = float('inf')
        cur = 0 
        L = 0
        for R in range(len(nums)):
            cur+=nums[R]
            while cur>=target:
                mn = min(mn, R-L+1)
                cur-=nums[L]
                L+=1
        return mn if mn!=float('inf') else 0