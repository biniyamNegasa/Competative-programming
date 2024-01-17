class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        cur = 0
        for n in nums:
            cur+=n
            ans.append(cur)
        return ans