class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        numDict={}
        for i,num in enumerate(nums):
            numDict[num]=i
        for prev,now in operations:
            nums[numDict[prev]]=now
            numDict[now]=numDict[prev]
        return nums
