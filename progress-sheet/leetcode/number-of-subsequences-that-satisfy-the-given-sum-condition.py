class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        ans = 0
        for i,n in enumerate(nums):
            ind = bisect_right(nums, target-n)-1
            exp = ind-i
            if exp>=0:
                ans += pow(2,exp)%MOD

        return ans%(MOD)