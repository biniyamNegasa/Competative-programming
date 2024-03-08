class Solution:
    def part(self, nums, target):
        count = 1
        curr = 0
        mx = 0
        for n in nums:
            curr+=n
            if curr>target:
                mx = max(curr-n, mx)
                count+=1
                curr = n
        mx = max(curr, mx)
        return count,mx
    def splitArray(self, nums: List[int], k: int) -> int:
        
        left = max(nums)
        right = sum(nums)
        ans = float('inf')
        while left<=right:
            mid = (left+right)//2
            t,mx = self.part(nums, mid)
            if t>k:
                left = mid+1
            else:
                ans = min(ans,mx)
                right = mid-1
        return ans