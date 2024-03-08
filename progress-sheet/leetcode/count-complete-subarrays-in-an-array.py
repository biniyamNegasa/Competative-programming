class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        check=len(set(nums))
        ans = 0
        L = 0
        dic_win = defaultdict(int)
        for R in range(n):
            dic_win[nums[R]]+=1
            while len(dic_win)==check:
                ans += n-R
                dic_win[nums[L]]-=1
                if not dic_win[nums[L]]:
                    del dic_win[nums[L]]
                L+=1

        return ans