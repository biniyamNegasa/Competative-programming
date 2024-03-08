class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        curr = 0
        patch = 0
        for num in nums:
            while curr+1<num and curr<n:
                patch+=1
                curr+= curr+1
            curr+=num
            if curr>=n:
                return patch
        while curr<n:
            patch+=1
            curr+=curr+1
        return patch