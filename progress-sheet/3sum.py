class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n-2):
            L = i+1
            R = n-1
            target = -nums[i]
            while L<R:
                val = nums[L]+nums[R]
                if val==target:
                    ans.add((nums[i], nums[L], nums[R]))
                    L+=1
                    R-=1
                elif val>target:
                    R-=1
                else:
                    L+=1
            
        return ans
    