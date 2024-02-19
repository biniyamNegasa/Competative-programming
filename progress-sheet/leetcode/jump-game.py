class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        n = len(nums)-1
        for i in range(len(nums)-1):
            if mx==i and not nums[i]:
                return False
            mx = max(mx, i+nums[i])
            if mx>=n:
                return True
        return True
            