class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic={num:i for i,num in enumerate(nums)}
        for prev,now in operations:
            ind=dic[prev]
            nums[ind]=now
            dic[now]=ind
            
        return nums