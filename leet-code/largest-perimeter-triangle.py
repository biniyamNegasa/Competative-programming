class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        for i in range(len(nums)-2):
            pm=nums[i]+nums[i+1]+nums[i+2]
            s=pm/2
            if s>nums[i+2]:
                ans=max(ans, pm)
        return ans