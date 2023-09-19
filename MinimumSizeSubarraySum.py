class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mn=len(nums)+1
        s=0
        L=0
        for R in range(len(nums)):
            s+=nums[R]
            while s>=target:
                mn=min(mn,R-L+1)
                s-=nums[L]
                L+=1
            R+=1
        return 0 if mn==len(nums)+1 else mn
