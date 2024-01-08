class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        mx = 0
        L = 0
        for R in range(len(nums)):
            if not nums[R] and not k:
                while nums[L] and L<R:
                    L+=1
                if not nums[L]:
                    k+=1
                L+=1
            if not nums[R]:
                k-=1
            mx = max(mx, R-L+1)
        return mx
                