class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        mx = float('-inf')
        curr_sum = 0
        for i in range(k-1):
            curr_sum+=nums[i]
        for i in range(k-1, len(nums)):
            curr_sum += nums[i]
            mx = max(mx, curr_sum/k)
            curr_sum -= nums[i-k+1]
        return mx