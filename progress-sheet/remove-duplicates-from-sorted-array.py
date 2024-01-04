class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L=0
        R=1
        c = 0
        while R<len(nums):
            if nums[L]==nums[R]:
                nums[R]=101
                c+=1
            else:
                L=R
            R+=1
        nums.sort()
        return len(nums)-c