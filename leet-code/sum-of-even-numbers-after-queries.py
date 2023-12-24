class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        even_sum=sum([n for n in nums if n%2==0])
        for val,i in queries:
            if nums[i]%2==0:
                even_sum-=nums[i]
            nums[i]+=val
            if nums[i]%2==0:
                even_sum+=nums[i]
            ans.append(even_sum)
        return ans