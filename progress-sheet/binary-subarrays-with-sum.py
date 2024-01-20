class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        L = 0
        curr = 0
        prev = 0
        ans = 0
        if goal:
            for R in range(n):
                curr+=nums[R]
                while curr>goal:
                    curr-=nums[L]
                    prev = 0
                    L+=1
                while L<R and curr==goal:
                    if nums[L]:
                        break
                    prev+=1
                    L+=1
                if curr==goal:
                    ans += prev+1
        else:
            for R in range(n):
                curr+=nums[R]
                while curr:
                    curr-=nums[L]
                    L+=1
                    i=0
                ans += R-L+1
        return ans