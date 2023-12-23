class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ng=[n for n in nums if n<0]
        ps=[n for n in nums if n>0]
        L=0
        ans=[]
        while L<len(ps):
            ans.append(ps[L])
            ans.append(ng[L])
            L+=1
        return ans