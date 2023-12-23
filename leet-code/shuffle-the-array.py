class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[]
        L=0
        R=n
        while L<n:
            ans.append(nums[L])
            ans.append(nums[R])
            L+=1
            R+=1
        return ans