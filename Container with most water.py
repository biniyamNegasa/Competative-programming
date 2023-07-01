class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        s=0
        while left<right:
            b=min(height[left],height[right])
            a=(right-left)*b
            if a>s:
                s=a
            if b==height[left]:
                left+=1
            else:
                right-=1
        return s
