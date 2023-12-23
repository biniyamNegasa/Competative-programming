class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        const=len(nums)//3
        ans=[]
        for n in count:
            if count[n]>const:
                ans.append(n)
        return ans