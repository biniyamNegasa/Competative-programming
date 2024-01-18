class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        L = 0
        prev = 0
        ans = 0
        for R in range(len(nums)):
            while not k and nums[R]%2==1:
                prev = 0
                if nums[L]%2==1:
                    k+=1
                L+=1
            if nums[R]%2==1:
                k-=1
            if not k:
                while nums[L]%2==0:
                    prev+=1
                    L+=1
                ans += prev+1
        return ans