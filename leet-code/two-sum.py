class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic=defaultdict(list)
        for i,n in enumerate(nums):
            dic[n].append(i)
        nums.sort()
        L=0
        R=len(nums)-1
        while L<R:
            temp=nums[L]+nums[R]
            if temp==target:
                i=dic[nums[L]].pop(0)
                j=dic[nums[R]].pop(0)
                return [i,j]
            elif temp>target:
                R-=1
            else:
                L+=1