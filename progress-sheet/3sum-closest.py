class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mn = float('inf')
        ans = 0
        nums.sort()
        for i in range(n-2):
            L = i+1
            R = n-1
            while L<R:
                val = target-nums[i]
                temp = abs(val-(nums[L]+nums[R]))
                if temp<mn:
                    mn = temp
                    ans = nums[i]+nums[L]+nums[R]
                if nums[L]+nums[R]<val:
                    L+=1
                else:
                    R-=1
        return ans