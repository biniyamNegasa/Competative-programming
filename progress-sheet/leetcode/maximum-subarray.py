class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        ans = float('-inf')
        for n in nums:
            curr = max(curr,0)+n
            ans = max(ans, curr)
        return ans