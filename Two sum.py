class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=[]
        for i in range(len(nums)):
            u=target-nums[i]
            for j in range(len(nums)):
                if nums[j]==u and i!=j:
                    a=[i,j]
                    return a
