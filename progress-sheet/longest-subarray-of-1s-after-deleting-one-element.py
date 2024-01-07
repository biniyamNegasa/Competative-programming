class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = 0
        L=0
        k = 1
        c = 0
        for R in range(len(nums)):
            if not nums[R]:
                if k:
                    k-=1
                else:
                    mx = max(mx, R-L-1)
                    L=c
                c = R+1
            mx = max(mx, R-L)
        return mx