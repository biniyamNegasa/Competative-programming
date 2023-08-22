class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefixSum=[]
        for num in nums:
            if prefixSum:
                prefixSum.append(prefixSum[-1]+num)
            else:
                prefixSum.append(num)
        return prefixSum
