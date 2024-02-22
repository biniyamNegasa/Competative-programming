class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stk = []
        for i, n in enumerate(temperatures):
            while stk and temperatures[stk[-1]]<n:
                ind = stk.pop()
                ans[ind] = i-ind
            stk.append(i)
        return ans