class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        inc_stk = []
        dec_stk = []
        idx = 0
        for n in arr:
            if inc_stk and inc_stk[-1]>=n:
                break
            inc_stk.append(n)
            idx+=1
        dec_stk.append(arr[idx-1])
        for i in range(idx, len(arr)):
            if dec_stk and dec_stk[-1]<=arr[i]:
                break
            dec_stk.append(arr[i])
        return len(inc_stk)+len(dec_stk)-1==len(arr) and len(dec_stk)>1 and len(inc_stk)>1