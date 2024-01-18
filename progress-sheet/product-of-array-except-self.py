class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_mult = [1]
        for n in nums:
            pre_mult.append(n*pre_mult[-1])
        post_mult = [1]
        for i in range(len(nums)-1,0,-1):
            post_mult.append(post_mult[-1]*nums[i])
        ans = []
        post_mult.reverse()
        for i in range(len(nums)):
            ans.append(pre_mult[i]*post_mult[i])
        return ans