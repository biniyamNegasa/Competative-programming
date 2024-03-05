class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []

        for i,n in enumerate(heights):
            while stack and heights[stack[-1]]>n:
                ind = stack.pop()
                sz = i-(stack[-1] if stack else -1)-1
                ans = max(ans, sz*heights[ind])
            stack.append(i)
        while stack:
            ind = stack.pop()
            sz = len(heights)-(stack[-1] if stack else -1)-1
            ans = max(ans, sz*heights[ind])
        return ans