class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        curr = 0
        ans = 0
        for i, n in enumerate(flips):
            curr += n
            m = (i+1)*(i+2)/2
            if curr==m:
                ans+=1
        return ans