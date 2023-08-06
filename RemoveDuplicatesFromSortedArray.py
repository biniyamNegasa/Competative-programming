class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left=0
        right=1
        while right<len(nums):
            if nums[left]==nums[right]:
                nums[right]=102
            else:
                left=right
            right+=1
        nums.sort()
        k=0
        for num in nums:
            if num!=102:
                k+=1
            else:
                break
        return k
