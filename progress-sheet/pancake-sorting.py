class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        n=len(arr)
        for _ in range(len(arr)):
            idx=arr.index(n)
            if not idx:
                arr=list(reversed(arr[:n]))+arr[n:]
                ans.append(n)
            elif idx!=n-1:
                arr=list(reversed(arr[:idx+1]))+arr[idx+1:]
                ans.append(idx+1)
                arr=list(reversed(arr[:n]))+arr[n:]
                ans.append(n)
            n-=1
        return ans