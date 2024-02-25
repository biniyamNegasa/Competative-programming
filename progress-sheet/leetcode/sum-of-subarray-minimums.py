class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stk = []
        ans = 0
        for i, n in enumerate(arr):
            while stk and arr[stk[-1]]>n:
                ind = stk.pop()
                bk = ind-(stk[-1] if stk else -1)
                front = i-ind
                ans+=bk*front*(arr[ind])
            stk.append(i)
        while stk:
            ind = stk.pop()
            bk = ind-(stk[-1] if stk else -1)
            front = len(arr)-ind
            ans+=bk*front*(arr[ind])
        return ans%(10**9 + 7)