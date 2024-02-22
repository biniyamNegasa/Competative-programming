class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans = 0
        for i in range(len(nums)):
            L = i+1
            R = len(nums)-1
            while L<R:
                if nums[L]+nums[R]>nums[i]:
                    ans += R-L
                    L+=1
                else:
                    R-=1
        return ans