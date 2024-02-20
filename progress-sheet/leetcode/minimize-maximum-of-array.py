class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        mx = nums[0]
        curr = mx
        for i in range(1, len(nums)):
            curr+=nums[i]
            if nums[i]>mx:
                mx = max(mx, ceil(curr/(i+1)))
        return mx