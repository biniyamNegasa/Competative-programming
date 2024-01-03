class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic={}
        for i,n in enumerate(sorted(nums)):
            if n not in dic:
                dic[n]= i
        return [dic[n] for n in nums]