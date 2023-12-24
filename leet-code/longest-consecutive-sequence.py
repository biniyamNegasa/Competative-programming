class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(list(set(nums)))
        ans=1
        cur_sum=1
        if not nums:
            return 0
        for i in range(1,len(nums)):
            if nums[i]-1<=nums[i-1]:
                cur_sum+=1
            else:
                cur_sum=1
            ans=max(ans, cur_sum)
        return ans