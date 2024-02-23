class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = nums[0]
        if not mx and len(nums)>1:
            return False
        for i, n in enumerate(nums[1:len(nums)-1]):
            if not n and mx==i+1:
                return False
            mx = max(mx, i+n+1)
        return True