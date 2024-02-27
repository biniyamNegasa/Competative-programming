class Solution:
    def trap(self, height: List[int]) -> int:
        stk = []
        ans = 0
        for i, n in enumerate(height):
            while stk and height[stk[-1]]<=n:
                ind = stk.pop()
                if stk:
                    mn = min(n,height[stk[-1]])
                    val = mn-height[ind]
                    dist = i-stk[-1]-1
                    ans += val*dist
            stk.append(i)
        return ans