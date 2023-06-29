class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst=[]
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                if i!=j and nums[i]>nums[j]:
                    c+=1
            lst.append(c)
        return lst
