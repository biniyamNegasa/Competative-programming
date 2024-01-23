class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n<3:
            return False
        mn = nums[0]
        mx_arr = []
        mx = nums[-1]
        for m in nums[n-1:1:-1]:
            mx = max(mx, m)
            mx_arr.append(mx)
        mx_arr.reverse()
        for R in range(1, n-1):
            mx = mx_arr[R-1]
            if mn<nums[R]<mx:
                return True
            mn = min(mn, nums[R])
            
        return False